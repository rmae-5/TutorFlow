# Documentación del Cliente Python de TutorFlow

Este documento describe el script clienteTutorFlow.py, un cliente de línea de comandos para interactuar con la API REST del servidor TutorFlow.

## Introducción

clienteTutorFlow.py es un script Python que permite a los usuarios realizar diversas operaciones en la API de TutorFlow, como listar, crear, actualizar y eliminar notificaciones, recursos y tareas. Proporciona una interfaz de menú interactiva para facilitar su uso.

## Configuración

La URL base de la API se define en la variable API_BASE_URL dentro del script. Si el servidor Spring Boot se ejecuta en un puerto diferente o en una dirección IP distinta, deberás ajustar esta variable.

python
API_BASE_URL = "http://localhost:8100/api"  # Cambia el puerto si es necesario


## Funciones Disponibles

El cliente Python implementa las siguientes funciones para interactuar con la API:

### listar_notificaciones()

*   *Descripción:* Obtiene todas las notificaciones.
*   *Uso:* Opción "1. Listar todas las notificaciones".

### listar_notificaciones_usuario(id_usuario)

*   *Descripción:* Obtiene las notificaciones de un usuario específico.
*   *Parámetros:* id_usuario (String).
*   *Uso:* Opción "2. Listar notificaciones por usuario".

### listar_recursos(materia=None)

*   *Descripción:* Obtiene todos los recursos, con filtro opcional por materia.
*   *Parámetros:* materia (String, opcional).
*   *Uso:* Opción "3. Listar recursos académicos".

### listar_tareas()

*   *Descripción:* Obtiene todas las tareas.
*   *Uso:* Opción "4. Listar tareas".

### obtener_tarea(id_tarea)

*   *Descripción:* Obtiene una tarea por su ID.
*   *Parámetros:* id_tarea (String).
*   *Uso:* Opción "5. Consultar tarea por ID".

### crear_notificacion(id_usuario, mensaje, fecha_iso=None)

*   *Descripción:* Crea una nueva notificación.
*   *Parámetros:* id_usuario (int), mensaje (str), fecha_iso (str, opcional).
*   *Uso:* Opción "6. Crear notificación".

### actualizar_notificacion(id_notificacion, ...)

*   *Descripción:* Actualiza una notificación existente.
*   *Parámetros:* id_notificacion (int) y campos opcionales.
*   *Uso:* Opción "7. Actualizar notificación".

### eliminar_notificacion(id_notificacion)

*   *Descripción:* Elimina una notificación.
*   *Parámetros:* id_notificacion (int).
*   *Uso:* Opción "8. Eliminar notificación".

### crear_recurso(titulo, descripcion, materia)

*   *Descripción:* Crea un nuevo recurso.
*   *Parámetros:* titulo (str), descripcion (str), materia (str).
*   *Uso:* Opción "9. Crear recurso".

### actualizar_recurso(id_recurso, ...)

*   *Descripción:* Actualiza un recurso existente.
*   *Parámetros:* id_recurso (int) y campos opcionales.
*   *Uso:* Opción "10. Actualizar recurso".

### eliminar_recurso(id_recurso)

*   *Descripción:* Elimina un recurso.
*   *Parámetros:* id_recurso (int).
*   *Uso:* Opción "11. Eliminar recurso".

### crear_tarea(titulo, descripcion, fecha_entrega_iso)

*   *Descripción:* Crea una nueva tarea.
*   *Parámetros:* titulo (str), descripcion (str), fecha_entrega_iso (str).
*   *Uso:* Opción "12. Crear tarea".

### actualizar_tarea(id_tarea, ...)

*   *Descripción:* Actualiza una tarea existente.
*   *Parámetros:* id_tarea (int) y campos opcionales.
*   *Uso:* Opción "13. Actualizar tarea".

### eliminar_tarea(id_tarea)

*   *Descripción:* Elimina una tarea.
*   *Parámetros:* id_tarea (int).
*   *Uso:* Opción "14. Eliminar tarea".

## Uso del Cliente (Menú Interactivo)

Al ejecutar el script, se presentará el siguiente menú:


========== CLIENTE TUTORFLOW ==========
1. Listar todas las notificaciones
2. Listar notificaciones por usuario
3. Listar recursos académicos
4. Listar tareas
5. Consultar tarea por ID
6. Crear notificación
7. Actualizar notificación
8. Eliminar notificación
9. Crear recurso
10. Actualizar recurso
11. Eliminar recurso
12. Crear tarea
13. Actualizar tarea
14. Eliminar tarea
0. Salir
Seleccione una opción:


## Cómo Ejecutar

Navega hasta el directorio TutorFlow/cliente-python/ y ejecuta:

```bash
python clienteTutorFlow.py
