# Documentación del Cliente Python de TutorFlow

Este documento describe el script `clienteTutorFlow.py`, un cliente de línea de comandos para interactuar con la API REST del servidor TutorFlow.

## Introducción

`clienteTutorFlow.py` es un script Python que permite a los usuarios realizar diversas operaciones en la API de TutorFlow, como listar notificaciones, recursos y tareas. Proporciona una interfaz de menú interactiva para facilitar su uso.

## Configuración

La URL base de la API se define en la variable `API_BASE_URL` dentro del script. Si el servidor Spring Boot se ejecuta en un puerto diferente o en una dirección IP distinta, deberás ajustar esta variable en el archivo `clienteTutorFlow.py` (aunque la solicitud es no tocar ningún archivo, esto es solo para información del usuario si necesita cambiarlo).

```python
API_BASE_URL = "http://localhost:8100/api"  # Cambia el puerto si es necesario
```

## Funciones Disponibles

El cliente Python implementa las siguientes funciones para interactuar con la API:

### `listar_notificaciones()`

*   **Descripción:** Realiza una solicitud GET a `/notificaciones` para obtener todas las notificaciones disponibles en el sistema.
*   **Uso:** Selecciona la opción "1. Listar todas las notificaciones" en el menú.

### `listar_notificaciones_usuario(id_usuario)`

*   **Descripción:** Realiza una solicitud GET a `/notificaciones/{idUsuario}` para obtener las notificaciones de un usuario específico.
*   **Parámetros:**
    *   `id_usuario` (String): El identificador único del usuario.
*   **Uso:** Selecciona la opción "2. Listar notificaciones por usuario" en el menú y proporciona el ID de usuario cuando se solicite.

### `listar_recursos(materia=None)`

*   **Descripción:** Realiza una solicitud GET a `/recursos` para obtener todos los recursos académicos. Opcionalmente, puede filtrar los recursos por materia.
*   **Parámetros:**
    *   `materia` (String, opcional): El nombre de la materia por la que se desea filtrar los recursos. Si no se proporciona, se listarán todos los recursos.
*   **Uso:** Selecciona la opción "3. Listar recursos académicos" en el menú. Se te preguntará si deseas filtrar por materia.

### `listar_tareas()`

*   **Descripción:** Realiza una solicitud GET a `/tareas` para obtener una lista de todas las tareas disponibles.
*   **Uso:** Selecciona la opción "4. Listar tareas" en el menú.

### `obtener_tarea(id_tarea)`

*   **Descripción:** Realiza una solicitud GET a `/tareas/{idTarea}` para obtener los detalles de una tarea específica.
*   **Parámetros:**
    *   `id_tarea` (String): El identificador único de la tarea.
*   **Uso:** Selecciona la opción "5. Consultar tarea por ID" en el menú y proporciona el ID de la tarea cuando se solicite.

## Uso del Cliente (Menú Interactivo)

Al ejecutar el script, se presentará un menú interactivo en la consola:

```
========== CLIENTE TUTORFLOW ==========
1. Listar todas las notificaciones
2. Listar notificaciones por usuario
3. Listar recursos académicos
4. Listar tareas
5. Consultar tarea por ID
0. Salir
Seleccione una opción:
```

Ingresa el número correspondiente a la opción deseada y presiona Enter. Sigue las instrucciones en pantalla para proporcionar cualquier parámetro requerido.

## Cómo Ejecutar

Para ejecutar el cliente Python, asegúrate de tener Python instalado en tu sistema. Luego, navega hasta el directorio `TutorFlow/cliente-python/` en tu terminal y ejecuta el siguiente comando:

```bash
python clienteTutorFlow.py
