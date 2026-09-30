from datetime import datetime
from src.services.agencia_service import AgenciaService
from src.core.exceptions import AgenciaException

class ConsoleUI:
    def __init__(self, service: AgenciaService):
        self.service = service
        self.usuario_actual = None

    def run(self):
        while True:
            print("\n" + "="*50)
            usuario_str = self.usuario_actual.nombre if self.usuario_actual else 'Ninguno'
            print(f"🚀 PANEL DE ADMINISTRACIÓN DE VIAJES (Usuario: {usuario_str})")
            print("="*50)
            print("0. Iniciar sesión (Seleccionar usuario)")
            print("1. Ver viajes disponibles")
            print("2. Registrar nuevo viaje")
            print("3. Registrar nueva reserva")
            print("4. Registrar nuevo usuario")
            print("5. Limpiar viajes finalizados")
            print("6. Salir")
            print("="*50)
            
            opcion = input("Selecciona una opción: ").strip()
            
            try:
                if opcion == '0':
                    self._iniciar_sesion()
                elif opcion == '1':
                    self._mostrar_viajes()
                elif opcion == '2':
                    self._registrar_viaje()
                elif opcion == '3':
                    self._registrar_reserva()
                elif opcion == '4':
                    self._registrar_usuario()
                elif opcion == '5':
                    self._limpiar_viajes()
                elif opcion == '6':
                    print("Saliendo del sistema...")
                    break
                else:
                    print("❌ Opción inválida.")
            except AgenciaException as e:
                print(f"⚠️ Error de validación: {e}")
            except Exception as e:
                print(f"💥 Error inesperado: {e}")

    def _iniciar_sesion(self):
        print("\n--- INICIO DE SESIÓN ---")
        nombre = input("Nombre: ")
        email = input("Email: ")
        usuario = self.service.autenticar_usuario(nombre, email)
        if usuario:
            self.usuario_actual = usuario
            print(f"✅ Bienvenido, {usuario.nombre}! (ID: {usuario.id_usuario})")
        else:
            print("❌ Usuario no encontrado. Verifica tu nombre y correo o regístrate en la opción 4.")

    def _mostrar_viajes(self):
        viajes = self.service.obtener_todos_los_viajes()
        if not viajes:
            print("No hay viajes disponibles.")
            return
            
        print("\nOpciones de visualización:")
        print("1. Local")
        print("2. Internacional")
        print("3. Todos")
        tipo_op = input("Seleccione el tipo de viaje: ").strip()
        
        tipo_filtro = None
        if tipo_op == '1':
            tipo_filtro = "Local"
            origen_filtro = input("Ingrese su punto de salida (Origen) para ver destinos directos permitidos: ").strip().lower()
        elif tipo_op == '2':
            tipo_filtro = "Internacional"
            
        viajes_filtrados = []
        for v in viajes:
            if tipo_filtro == "Local" and v.tipo == "Local":
                if v.origen.lower() == origen_filtro:
                    viajes_filtrados.append(v)
            elif tipo_filtro == "Internacional" and v.tipo == "Internacional":
                viajes_filtrados.append(v)
            elif tipo_op not in ['1', '2']:
                viajes_filtrados.append(v)

        if not viajes_filtrados:
            print("No se encontraron viajes con esos criterios.")
            return

        for v in viajes_filtrados:
            print(f"\n✈️  VIAJE #{v.id_viaje}: [{v.tipo}] {v.origen} -> {v.destino} ({v.fecha_inicio} a {v.fecha_fin}) - €{v.precio}")
            reservas = self.service.obtener_reservas_por_viaje(v.id_viaje)
            if reservas:
                print("   Reservas:")
                for r in reservas:
                    print(f"    - #{r.id_reserva}: {r.nombre_cliente} ({r.plazas} plazas)")
            else:
                print("   (Sin reservas registradas)")

    def _registrar_viaje(self):
        origen = input("Punto de salida (Origen): ")
        destino = input("Destino: ")
        f_inicio = datetime.strptime(input("Fecha inicio (AAAA-MM-DD): "), "%Y-%m-%d").date()
        f_fin = datetime.strptime(input("Fecha fin (AAAA-MM-DD): "), "%Y-%m-%d").date()
        precio = float(input("Precio: "))
        tipo = input("Tipo (Local/Internacional): ").strip().capitalize()
        if tipo not in ["Local", "Internacional"]:
            tipo = "Internacional"
        
        v = self.service.agregar_viaje(origen, destino, f_inicio, f_fin, precio, tipo)
        print(f"✅ Viaje #{v.id_viaje} de {v.origen} a {v.destino} ({v.tipo}) registrado con éxito.")

    def _registrar_reserva(self):
        viajes = self.service.obtener_todos_los_viajes()
        if not viajes:
            print("No hay viajes disponibles para reservar.")
            return
            
        print("\n--- VIAJES DISPONIBLES PARA RESERVAR ---")
        for v in viajes:
            print(f"[{v.id_viaje}] {v.origen} -> {v.destino} ({v.fecha_inicio} a {v.fecha_fin}) - €{v.precio}")
            
        id_viaje = int(input("\nIngresa el ID del Viaje en el que quieres reservar: "))
        cliente = input("Nombre del cliente: ")
        plazas = int(input("Número de plazas: "))
        
        r = self.service.agregar_reserva(id_viaje, cliente, plazas)
        print(f"✅ Reserva #{r.id_reserva} creada.")

    def _registrar_usuario(self):
        nombre = input("Nombre: ")
        email = input("Email: ")
        pais = input("País de tu número de teléfono (ej. +34, +57, +52): ").strip()
        tel_num = input("Número de Teléfono (10 dígitos): ").strip()
        tel = f"{pais} {tel_num}" if pais else tel_num
        u = self.service.registrar_usuario(nombre, email, tel)
        print(f"✅ Usuario #{u.id_usuario} ({u.nombre}) registrado con número {u.telefono}.")

    def _limpiar_viajes(self):
        eliminados = self.service.limpiar_viajes_finalizados()
        print(f"🧹 Se han limpiado {eliminados} viajes finalizados.")
