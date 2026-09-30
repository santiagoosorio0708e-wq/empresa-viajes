import sqlite3
import random
from datetime import date, timedelta
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "agencia.db"

def seed_db():
    if not DB_PATH.exists():
        print("La base de datos no existe. Ejecuta el programa principal primero.")
        return

    # Delete existing data in viajes for a clean slate
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Try recreating the table if the schema was old
    cursor.execute("DROP TABLE IF EXISTS prestamos_carro")
    cursor.execute("DROP TABLE IF EXISTS reservas")
    cursor.execute("DROP TABLE IF EXISTS viajes")
    
    cursor.execute('''
        CREATE TABLE viajes (
            id_viaje INTEGER PRIMARY KEY AUTOINCREMENT,
            origen TEXT NOT NULL,
            destino TEXT NOT NULL,
            fecha_inicio DATE NOT NULL,
            fecha_fin DATE NOT NULL,
            precio REAL NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')
    
    # We will recreate reservas and prestamos_carro as well to maintain integrity
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id_reserva INTEGER PRIMARY KEY AUTOINCREMENT,
            id_viaje INTEGER NOT NULL,
            nombre_cliente TEXT NOT NULL,
            plazas INTEGER NOT NULL,
            FOREIGN KEY(id_viaje) REFERENCES viajes(id_viaje) ON DELETE CASCADE
        )
    ''')
    
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

    viajes_seed = []
    hoy = date.today()
    
    # Generate 32 international trips
    paises_mundo = ["Francia", "Italia", "Alemania", "Japón", "EEUU", "Brasil", "Australia", "Canadá", "Egipto", "México", "Reino Unido", "Argentina", "Noruega", "Grecia", "Tailandia", "Sudáfrica", "Perú", "India", "Suiza", "Nueva Zelanda", "China", "Marruecos", "Turquía", "Corea del Sur", "Irlanda", "Rusia", "Portugal", "Holanda", "Suecia", "Polonia", "Colombia", "Chile"]
    ciudades_espana = ["Madrid", "Barcelona", "Valencia"]
    for i in range(32):
        origen = random.choice(ciudades_espana)
        destino = paises_mundo[i % len(paises_mundo)]
        inicio = hoy + timedelta(days=random.randint(10, 90))
        fin = inicio + timedelta(days=random.randint(5, 20))
        precio = random.randint(300, 2500)
        viajes_seed.append((origen, destino, inicio.isoformat(), fin.isoformat(), float(precio), "Internacional"))

    cursor.executemany(
        "INSERT INTO viajes (origen, destino, fecha_inicio, fecha_fin, precio, tipo) VALUES (?, ?, ?, ?, ?, ?)",
        viajes_seed
    )
    
    conn.commit()
    conn.close()
    print("Base de datos repoblada con 32 viajes.")

if __name__ == "__main__":
    seed_db()
