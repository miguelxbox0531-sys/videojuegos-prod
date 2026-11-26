 Mini-Sistema de Videojuegos

Este proyecto es el despliegue en producción de mi microaplicación de videojuegos con sistema de login. Utilicé Flask, MySQL y Docker para contenerizar todo y asegurar que funcione igual en cualquier entorno.

## Tecnologías usadas
*   **Python / Flask:** Backend y manejo de rutas.
*   **Flask-Login:** Para la autenticación y manejo de sesiones.
*   **MySQL 8.0:** Base de datos relacional.
*   **Gunicorn:** Servidor WSGI para producción.
*   **Docker y Docker Compose:** Orquestación de los contenedores.
*   **Git / GitHub:** Control de versiones.

## Pasos para levantar la aplicación en producción

1.  Clonar el repositorio:
    ```bash
    git clone https://github.com/miguelxbox0531-sys/videojuegos-prod.git
    cd videojuegos-prod