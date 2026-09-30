import sqlite3
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)

# Configurar ruta absoluta para la BD en la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "agencia.db"

def init_db():
    """Inicializa la base de datos y crea las tablas si no existen."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Tabla Usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            puntos INTEGER DEFAULT 0
        )
    ''')

    # Tabla Viajes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS viajes (
            id_viaje INTEGER PRIMARY KEY AUTOINCREMENT,
            origen TEXT NOT NULL,
            destino TEXT NOT NULL,
            fecha_inicio DATE NOT NULL,
            fecha_fin DATE NOT NULL,
            precio REAL NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')

    # Tabla Reservas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
            id_viaje INTEGER NOT NULL,
            nombre_cliente TEXT NOT NULL,
            plazas INTEGER NOT NULL,
            FOREIGN KEY(id_viaje) REFERENCES viajes(id_viaje) ON DELETE CASCADE
        )
    ''')

    # Tabla Prestamos de Carro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prestamos_carro (
            id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            id_viaje INTEGER NOT NULL,
            marca TEXT NOT NULL,
            dias_previstos INTEGER NOT NULL,
            dias_reales INTEGER NOT NULL,
            costo_total REAL NOT NULL,
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
            FOREIGN KEY(id_viaje) REFERENCES viajes(id_viaje) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    logger.info("Base de datos inicializada correctamente.")

def get_connection():
    """Devuelve una conexión a la base de datos."""
    return sqlite3.connect(DB_PATH)
