from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Usuario:
    nombre: str
    email: str
    telefono: str
    puntos: int = 0
    id_usuario: Optional[int] = None

@dataclass
class Viaje:
    origen: str
    destino: str
    fecha_inicio: date
    fecha_fin: date
    precio: float
    tipo: str  # "Local" o "Internacional"
    id_viaje: Optional[int] = None

@dataclass
class Reserva:
    id_viaje: int
    nombre_cliente: str
    plazas: int
    id_reserva: Optional[int] = None

@dataclass
class PrestamoCarro:
    id_usuario: int
    id_viaje: int
    marca: str
    dias_previstos: int
    dias_reales: int
    costo_total: float
    id_prestamo: Optional[int] = None
