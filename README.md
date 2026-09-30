<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">✈️ Agencia de Viajes - Agile Edition 🌍</h1>

  <p align="center">
    <strong>Sistema integral por consola para la gestión avanzada de agencias de viaje</strong>
    <br />
    <br />
    <a href="#uso"><strong>Explorar la documentación »</strong></a>
    <br />
    <br />
    <a href="#demo">Ver Demo</a>
    ·
    <a href="https://github.com/santiagoosorio0708e-wq/empresa-viajes/issues">Reportar un Bug</a>
    ·
    <a href="https://github.com/santiagoosorio0708e-wq/empresa-viajes/issues">Solicitar Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca del Proyecto</a>
      <ul>
        <li><a href="#construido-con">Construido con</a></li>
        <li><a href="#arquitectura-del-sistema">Arquitectura del Sistema</a></li>
      </ul>
    </li>
    <li>
      <a href="#comenzando">Comenzando</a>
      <ul>
        <li><a href="#prerrequisitos">Prerrequisitos</a></li>
        <li><a href="#instalación">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso y Características</a></li>
    <li><a href="#pruebas">Pruebas Unitarias</a></li>
    <li><a href="#hoja-de-ruta">Hoja de Ruta</a></li>
    <li><a href="#licencia">Licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ol>
</details>

---

## 📖 Acerca del Proyecto

Este proyecto nace con la necesidad de proporcionar una herramienta robusta y escalable para agencias de viajes a través de una interfaz de línea de comandos (CLI). Su núcleo está diseñado siguiendo principios de la arquitectura limpia (*Clean Architecture*), aislando la persistencia de datos (SQLite), de la lógica de negocio (Servicios) y los modelos de datos (Dataclasses).

El sistema se enfoca en resolver problemáticas del mundo real mediante validaciones estrictas y protección de integridad referencial para garantizar datos seguros y precisos.

### Construido con

Esta sección enlista las tecnologías principales que hacen posible el ecosistema del proyecto:

* [![Python][Python.org]][Python-url]
* [![SQLite][SQLite.org]][SQLite-url]

### Arquitectura del Sistema

El proyecto implementa el patrón **Repository** e **Inyección de Dependencias**, estructurando los módulos de la siguiente forma:

```text
📦 proyecto_empresa_de_viajes
 ┣ 📂 src
 ┃ ┣ 📂 core          👉 Dataclasses (Usuario, Viaje, Reserva) y Excepciones
 ┃ ┣ 📂 data          👉 Contextos de SQLite y capa de Repositorios (CRUD)
 ┃ ┣ 📂 services      👉 Casos de uso e interacciones de negocio centralizadas
 ┃ ┗ 📂 ui            👉 Menú de consola interactivo con persistencia de sesión
 ┣ 📂 tests           👉 Pruebas Unitarias exhaustivas de los servicios
 ┣ 📜 seed_db.py      👉 Motor de población de BD (Generador de Mock Data)
 ┗ 📜 main.py         👉 Punto de entrada e Inyección de Dependencias
```

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

---

## 🚀 Comenzando

A continuación, se detalla cómo configurar este proyecto localmente. Sigue los pasos para obtener una copia funcional.

### Prerrequisitos

Asegúrate de contar con Python instalado en su versión 3.9 o superior.
* Verificar instalación:
  ```sh
  python --version
  ```

### Instalación

1. Clona el repositorio
   ```sh
   git clone https://github.com/santiagoosorio0708e-wq/empresa-viajes.git
   ```
2. Navega al directorio del proyecto
   ```sh
   cd empresa-viajes
   ```
3. Inicializa la base de datos con información semilla (esto inyectará **32 viajes internacionales interactivos** listos para reservar)
   ```sh
   python seed_db.py
   ```
   *(Nota: En sistemas Windows, puedes utilizar el lanzador nativo `py seed_db.py`)*

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

---

## ⚡ Uso y Características

Una vez instalado, inicia la consola interactiva ejecutando:
```sh
python src/main.py
```

### Funciones Principales:
* 🔐 **Manejo de Sesiones Avanzado**: 
  * Los usuarios deben registrarse validando exactamente 10 dígitos numéricos e ingresando su código de país.
  * Autenticación local integrada. Persistencia de identidad durante el flujo de reserva.
* 🛡️ **Validaciones Anti-Fraude & Lógicas**:
  * Fechas de viaje imposibles bloqueadas (fecha fin menor a la de inicio).
  * Los destinos turísticos cuentan con unicidad (imposible duplicar registros).
* 🗂️ **Filtrado Dinámico en CLI**:
  * Capacidad de visualizar y separar rutas en base a viajes de carácter **Local** o **Internacional**, calculando orígenes y destinos.
* 🧹 **Mantenimiento Autónomo**:
  * Función nativa para detectar y eliminar automáticamente viajes que ya cumplieron sus fechas (Histórico), manteniendo la DB óptima.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

---

## 🧪 Pruebas Unitarias

El proyecto cuenta con un entorno seguro de pruebas integradas. Las bases de datos en los entornos de testing utilizan simulaciones en memoria (`sqlite3: :memory:`) para no contaminar la base de datos real en producción.

Ejecuta el test suite con:
```sh
python -m unittest tests/test_agencia_service.py
```
*Salida esperada: Todos los casos de éxito (OK)*

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

---

## 🗺️ Hoja de Ruta

- [x] Construcción del patrón repositorio.
- [x] Inyección de dependencias completada.
- [x] Scripts de repoblación automática (Seed).
- [x] Filtros interactivos de destinos locales vs internacionales.
- [ ] Exportación de reportes de reservas a CSV/Excel.
- [ ] Implementar un Front-End con React.JS acoplado a una API de FastAPI.

Consulta los [Issues abiertos](https://github.com/santiagoosorio0708e-wq/empresa-viajes/issues) para una lista completa de características propuestas (y problemas conocidos).

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

---

## 📄 Licencia

Distribuido bajo la licencia MIT. Consulta el archivo `LICENSE.txt` para más información.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

---

## 📬 Contacto

**Santiago Osorio** - Desarrollador Principal - [Perfil de GitHub](https://github.com/santiagoosorio0708e-wq)

Link del Proyecto: [https://github.com/santiagoosorio0708e-wq/empresa-viajes](https://github.com/santiagoosorio0708e-wq/empresa-viajes)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/santiagoosorio0708e-wq/empresa-viajes.svg?style=for-the-badge
[contributors-url]: https://github.com/santiagoosorio0708e-wq/empresa-viajes/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/santiagoosorio0708e-wq/empresa-viajes.svg?style=for-the-badge
[forks-url]: https://github.com/santiagoosorio0708e-wq/empresa-viajes/network/members
[stars-shield]: https://img.shields.io/github/stars/santiagoosorio0708e-wq/empresa-viajes.svg?style=for-the-badge
[stars-url]: https://github.com/santiagoosorio0708e-wq/empresa-viajes/stargazers
[issues-shield]: https://img.shields.io/github/issues/santiagoosorio0708e-wq/empresa-viajes.svg?style=for-the-badge
[issues-url]: https://github.com/santiagoosorio0708e-wq/empresa-viajes/issues
[license-shield]: https://img.shields.io/github/license/santiagoosorio0708e-wq/empresa-viajes.svg?style=for-the-badge
[license-url]: https://github.com/santiagoosorio0708e-wq/empresa-viajes/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/santiagoosorio0708e-wq
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[SQLite.org]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[SQLite-url]: https://www.sqlite.org/
