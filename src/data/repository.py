import sqlite3
from typing import List, Optional
from datetime import datetime
from src.core.models import Usuario, Viaje, Reserva, PrestamoCarro
from src.core.exceptions import ElementoNoEncontradoError
from src.data.database import get_connection

class UsuarioRepository:
    def create(self, usuario: Usuario) -> Usuario:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, telefono, puntos) VALUES (?, ?, ?, ?)",
                (usuario.nombre, usuario.email, usuario.telefono, usuario.puntos)
            )
            usuario.id_usuario = cursor.lastrowid
            conn.commit()
            return usuario
            
    def get_all(self) -> List[Usuario]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios")
            rows = cursor.fetchall()
            return [Usuario(id_usuario=r[0], nombre=r[1], email=r[2], telefono=r[3], puntos=r[4]) for r in rows]

    def get_by_id(self, id_usuario: int) -> Optional[Usuario]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = ?", (id_usuario,))
            row = cursor.fetchone()
            if row:
                return Usuario(id_usuario=row[0], nombre=row[1], email=row[2], telefono=row[3], puntos=row[4])
            return None
            
    def get_by_name_and_email(self, nombre: str, email: str) -> Optional[Usuario]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND email = ?", (nombre, email))
            row = cursor.fetchone()
            if row:
                return Usuario(id_usuario=row[0], nombre=row[1], email=row[2], telefono=row[3], puntos=row[4])
            return None
            
    def update_puntos(self, id_usuario: int, puntos: int):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET puntos = ? WHERE id_usuario = ?", (puntos, id_usuario))
            conn.commit()

class ViajeRepository:
    def create(self, viaje: Viaje) -> Viaje:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO viajes (origen, destino, fecha_inicio, fecha_fin, precio, tipo) VALUES (?, ?, ?, ?, ?, ?)",
                (viaje.origen, viaje.destino, viaje.fecha_inicio.isoformat(), viaje.fecha_fin.isoformat(), viaje.precio, viaje.tipo)
            )
            viaje.id_viaje = cursor.lastrowid
            conn.commit()
            return viaje
            
    def get_all(self) -> List[Viaje]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM viajes")
            rows = cursor.fetchall()
            return [Viaje(
                id_viaje=r[0],
                origen=r[1],
                destino=r[2], 
                fecha_inicio=datetime.fromisoformat(r[3]).date(), 
                fecha_fin=datetime.fromisoformat(r[4]).date(), 
                precio=r[5],
                tipo=r[6]
            ) for r in rows]

    def get_by_id(self, id_viaje: int) -> Optional[Viaje]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM viajes WHERE id_viaje = ?", (id_viaje,))
            row = cursor.fetchone()
            if row:
                return Viaje(
                    id_viaje=row[0],
                    origen=row[1],
                    destino=row[2], 
                    fecha_inicio=datetime.fromisoformat(row[3]).date(), 
                    fecha_fin=datetime.fromisoformat(row[4]).date(), 
                    precio=row[5],
                    tipo=row[6]
                )
            return None

    def delete(self, id_viaje: int):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM viajes WHERE id_viaje = ?", (id_viaje,))
            conn.commit()

class ReservaRepository:
    def create(self, reserva: Reserva) -> Reserva:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO reservas (id_viaje, nombre_cliente, plazas) VALUES (?, ?, ?)",
                (reserva.id_viaje, reserva.nombre_cliente, reserva.plazas)
            )
            reserva.id_reserva = cursor.lastrowid
            conn.commit()
            return reserva
            
    def get_by_viaje(self, id_viaje: int) -> List[Reserva]:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservas WHERE id_viaje = ?", (id_viaje,))
            rows = cursor.fetchall()
            return [Reserva(id_reserva=r[0], id_viaje=r[1], nombre_cliente=r[2], plazas=r[3]) for r in rows]
