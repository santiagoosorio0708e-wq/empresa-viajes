# Agencia de Viajes - Agile Edition 🚀

Sistema integral por consola para la gestión de una agencia de viajes. Construido en **Python** con una arquitectura limpia basada en capas y persistencia en **SQLite**.

## Características Principales

* **Autenticación de Usuarios:** Sistema de inicio de sesión y registro interactivo que guarda sesión durante la ejecución.
* **Validación Robusta:** 
  * Validación de longitud exacta de números telefónicos (10 dígitos).
  * Solicitud de código de país.
  * Prevención de duplicidad de destinos turísticos.
* **Gestión de Viajes:** 
  * Diferenciación entre viajes **Locales** e **Internacionales**.
  * Filtrado dinámico de destinos según el origen del viaje.
* **Gestión de Reservas:** Interfaz visual para elegir el ID del viaje directamente de una tabla interactiva.
* **Arquitectura:**
  * Uso del **Patrón Repositorio** para abstraer el acceso a datos.
  * Inyección de dependencias en la capa de servicios.
  * Modelado de datos mediante `dataclasses`.

## Estructura del Proyecto

```
proyectoagenciaviajes/
├── src/
│   ├── core/           # Modelos de datos y Excepciones personalizadas
│   ├── data/           # Configuración de base de datos y repositorios (SQLite)
│   ├── services/       # Lógica de negocio
│   └── ui/             # Interfaz de usuario por consola
├── tests/              # Pruebas unitarias
├── seed_db.py          # Script de repoblación (32 viajes internacionales por defecto)
└── agencia.db          # Base de datos (generada automáticamente)
```

## Instalación y Uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/santiagoosorio0708e-wq/empresa-viajes.git
   cd empresa-viajes
   ```

2. (Opcional) Popula la base de datos con viajes de prueba:
   ```bash
   python seed_db.py
   ```
   *(Nota: En Windows puedes usar el comando `py seed_db.py`)*

3. Ejecuta la aplicación principal:
   ```bash
   python src/main.py
   ```
   *(Nota: En Windows puedes usar el comando `py src/main.py`)*

## Pruebas Unitarias

Para correr los tests integrados:
```bash
python -m unittest tests/test_agencia_service.py
```
