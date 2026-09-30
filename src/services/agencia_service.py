from datetime import date
from typing import List, Optional
from src.core.models import Usuario, Viaje, Reserva
from src.core.exceptions import ValidacionError, ElementoNoEncontradoError
from src.data.repository import UsuarioRepository, ViajeRepository, ReservaRepository

class AgenciaService:
    def __init__(self, usuario_repo: UsuarioRepository, viaje_repo: ViajeRepository, reserva_repo: ReservaRepository):
        self.usuario_repo = usuario_repo
        self.viaje_repo = viaje_repo
        self.reserva_repo = reserva_repo

    def registrar_usuario(self, nombre: str, email: str, telefono: str) -> Usuario:
        if not nombre or not email:
            raise ValidacionError("Nombre y email son requeridos")
            
        # Extraer el número sin el código de país para validarlo (ejemplo: +57 3001234567)
        # Asumimos que el usuario podría incluir el código de país con un espacio o directamente
        partes = telefono.strip().split()
        num_base = partes[-1] if len(partes) > 1 else telefono
        
        if len(num_base) != 10 or not num_base.isdigit():
            raise ValidacionError("El número de teléfono debe tener exactamente 10 dígitos (sin contar el código de país).")
            
        usuario = Usuario(nombre=nombre, email=email, telefono=telefono)
        return self.usuario_repo.create(usuario)

    def autenticar_usuario(self, nombre: str, email: str) -> Optional[Usuario]:
        return self.usuario_repo.get_by_name_and_email(nombre, email)

    def agregar_viaje(self, origen: str, destino: str, f_inicio: date, f_fin: date, precio: float, tipo: str) -> Viaje:
        if f_fin < f_inicio:
            raise ValidacionError("La fecha de fin no puede ser anterior a la de inicio.")
        if precio <= 0:
            raise ValidacionError("El precio debe ser mayor a 0.")
            
        # Validar que no se repita el destino
        viajes_existentes = self.viaje_repo.get_all()
        for v in viajes_existentes:
            if v.destino.lower() == destino.lower():
                raise ValidacionError(f"Ya existe un viaje registrado hacia el destino '{destino}'.")
                
        viaje = Viaje(origen=origen, destino=destino, fecha_inicio=f_inicio, fecha_fin=f_fin, precio=precio, tipo=tipo)
        return self.viaje_repo.create(viaje)

    def agregar_reserva(self, id_viaje: int, nombre_cliente: str, plazas: int) -> Reserva:
        viaje = self.viaje_repo.get_by_id(id_viaje)
        if not viaje:
            raise ElementoNoEncontradoError(f"El viaje con id {id_viaje} no existe.")
        if plazas <= 0:
            raise ValidacionError("El número de plazas debe ser mayor a 0.")
            
        reserva = Reserva(id_viaje=id_viaje, nombre_cliente=nombre_cliente, plazas=plazas)
        return self.reserva_repo.create(reserva)

    def obtener_todos_los_viajes(self) -> List[Viaje]:
        return self.viaje_repo.get_all()

    def obtener_reservas_por_viaje(self, id_viaje: int) -> List[Reserva]:
        return self.reserva_repo.get_by_viaje(id_viaje)
        
    def limpiar_viajes_finalizados(self) -> int:
        hoy = date.today()
        viajes = self.viaje_repo.get_all()
        eliminados = 0
        for viaje in viajes:
            if viaje.fecha_fin < hoy:
                self.viaje_repo.delete(viaje.id_viaje)
                eliminados += 1
        return eliminados
