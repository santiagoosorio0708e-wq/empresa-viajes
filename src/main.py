import sys
import os

# Configurar la salida estándar para soportar caracteres especiales (emojis) en Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Asegurar que el path alcance los imports de src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
from src.data.database import init_db
from src.data.repository import UsuarioRepository, ViajeRepository, ReservaRepository
from src.services.agencia_service import AgenciaService
from src.ui.console_menu import ConsoleUI

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    print("Iniciando aplicación. Configurando Base de Datos...")
    init_db()
    
    # Inyección de dependencias
    usuario_repo = UsuarioRepository()
    viaje_repo = ViajeRepository()
    reserva_repo = ReservaRepository()
    
    servicio = AgenciaService(usuario_repo, viaje_repo, reserva_repo)
    ui = ConsoleUI(servicio)
    
    # Lanzar la aplicación
    ui.run()

if __name__ == "__main__":
    main()
