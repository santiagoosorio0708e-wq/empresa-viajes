import sys
import os
import sqlite3
import unittest
from datetime import date, timedelta

# Asegurar que importamos src correctamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.data.database as db
from src.data.repository import UsuarioRepository, ViajeRepository, ReservaRepository
from src.services.agencia_service import AgenciaService
from src.core.exceptions import ValidacionError

# Sobrescribir get_connection para usar memoria durante los tests
from unittest.mock import patch

# Usar una única conexión en memoria compartida para los tests
_mock_conn = sqlite3.connect(':memory:', check_same_thread=False)

def mock_get_connection():
    return _mock_conn

class TestAgenciaService(unittest.TestCase):
    def setUp(self):
        # Patch the get_connection exactly where it is imported/used
        self.patcher1 = patch('src.data.database.get_connection', side_effect=mock_get_connection)
        self.patcher2 = patch('src.data.repository.get_connection', side_effect=mock_get_connection)
        self.patcher1.start()
        self.patcher2.start()
        
        # Configurar DB en memoria (esto usará el get_connection patcheado)
        db.init_db()
        self.u_repo = UsuarioRepository()
        self.v_repo = ViajeRepository()
        self.r_repo = ReservaRepository()
        self.servicio = AgenciaService(self.u_repo, self.v_repo, self.r_repo)

    def tearDown(self):
        # Limpiar datos para evitar colisiones entre tests
        with _mock_conn:
            _mock_conn.execute("DELETE FROM usuarios")
            _mock_conn.execute("DELETE FROM viajes")
            _mock_conn.execute("DELETE FROM reservas")
        self.patcher1.stop()
        self.patcher2.stop()

    def test_registrar_usuario_exitoso(self):
        u = self.servicio.registrar_usuario("Juan", "juan@test.com", "3001234567")
        self.assertIsNotNone(u.id_usuario)
        self.assertEqual(u.nombre, "Juan")

    def test_registrar_usuario_sin_email_lanza_error(self):
        with self.assertRaises(ValidacionError):
            self.servicio.registrar_usuario("Juan", "", "123")

    def test_agregar_viaje_fechas_invalidas(self):
        inicio = date.today()
        fin = inicio - timedelta(days=1)
        with self.assertRaises(ValidacionError):
            self.servicio.agregar_viaje("Madrid", "Barcelona", inicio, fin, 1000, "Local")

    def test_limpiar_viajes_finalizados(self):
        # Crear viaje pasado
        pasado_inicio = date.today() - timedelta(days=10)
        pasado_fin = date.today() - timedelta(days=5)
        self.servicio.agregar_viaje("Madrid", "Roma", pasado_inicio, pasado_fin, 500, "Internacional")
        
        # Crear viaje futuro
        futuro_inicio = date.today() + timedelta(days=5)
        futuro_fin = date.today() + timedelta(days=10)
        self.servicio.agregar_viaje("Madrid", "Paris", futuro_inicio, futuro_fin, 600, "Internacional")
        
        viajes = self.servicio.obtener_todos_los_viajes()
        self.assertEqual(len(viajes), 2)
        
        eliminados = self.servicio.limpiar_viajes_finalizados()
        self.assertEqual(eliminados, 1)
        
        viajes_actualizados = self.servicio.obtener_todos_los_viajes()
        self.assertEqual(len(viajes_actualizados), 1)
        self.assertEqual(viajes_actualizados[0].destino, "Paris")

if __name__ == '__main__':
    unittest.main()
