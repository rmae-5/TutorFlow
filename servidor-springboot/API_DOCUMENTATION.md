# Documentación de la API REST de TutorFlow - Servidor Spring Boot

Este documento describe los endpoints y modelos de datos de la API REST del servidor Spring Boot de TutorFlow.

## Endpoints

### Notificaciones

Gestiona las notificaciones de los usuarios.

*   **`GET /notificaciones`**
    *   **Descripción:** Obtiene una lista de todas las notificaciones.
    *   **Respuestas:**
        *   `200 OK`: Lista de objetos `Notificacion`.

*   **`GET /notificaciones/{idUsuario}`**
    *   **Descripción:** Obtiene una lista de notificaciones para un usuario específico.
    *   **Parámetros de Ruta:**
        *   `idUsuario` (Long): El ID del usuario.
    *   **Respuestas:**
        *   `200 OK`: Lista de objetos `Notificacion` para el usuario especificado.
        *   `404 Not Found`: Si no se encuentran notificaciones para el usuario.

*   **`POST /notificaciones`**
    *   **Descripción:** Crea una nueva notificación.
    *   **Cuerpo de la Solicitud:** Objeto `Notificacion` (sin `id`).
    *   **Respuestas:**
        *   `200 OK`: La `Notificacion` creada.

*   **`PUT /notificaciones/{id}`**
    *   **Descripción:** Actualiza una notificación existente.
    *   **Parámetros de Ruta:**
        *   `id` (Long): El ID de la notificación a actualizar.
    *   **Cuerpo de la Solicitud:** Objeto `Notificacion` con los datos actualizados.
    *   **Respuestas:**
        *   `200 OK`: La `Notificacion` actualizada.
        *   `404 Not Found`: Si la notificación no se encuentra.

*   **`DELETE /notificaciones/{id}`**
    *   **Descripción:** Elimina una notificación por su ID.
    *   **Parámetros de Ruta:**
        *   `id` (Long): El ID de la notificación a eliminar.
    *   **Respuestas:**
        *   `204 No Content`: Si la notificación fue eliminada exitosamente.
        *   `404 Not Found`: Si la notificación no se encuentra.

### Recursos

Gestiona los recursos educativos.

*   **`GET /recursos`**
    *   **Descripción:** Obtiene una lista de todos los recursos o filtra por materia.
    *   **Parámetros de Consulta (Opcional):**
        *   `materia` (String): Filtra los recursos por el nombre de la materia.
    *   **Respuestas:**
        *   `200 OK`: Lista de objetos `Recurso`.

*   **`POST /recursos`**
    *   **Descripción:** Crea un nuevo recurso.
    *   **Cuerpo de la Solicitud:** Objeto `Recurso` (sin `id`).
    *   **Respuestas:**
        *   `200 OK`: El `Recurso` creado.

*   **`PUT /recursos/{id}`**
    *   **Descripción:** Actualiza un recurso existente.
    *   **Parámetros de Ruta:**
        *   `id` (Long): El ID del recurso a actualizar.
    *   **Cuerpo de la Solicitud:** Objeto `Recurso` con los datos actualizados.
    *   **Respuestas:**
        *   `200 OK`: El `Recurso` actualizado.
        *   `404 Not Found`: Si el recurso no se encuentra.

*   **`DELETE /recursos/{id}`**
    *   **Descripción:** Elimina un recurso por su ID.
    *   **Parámetros de Ruta:**
        *   `id` (Long): El ID del recurso a eliminar.
    *   **Respuestas:**
        *   `204 No Content`: Si el recurso fue eliminado exitosamente.
        *   `404 Not Found`: Si el recurso no se encuentra.

### Tareas

Gestiona las tareas asignadas.

*   **`GET /tareas`**
    *   **Descripción:** Obtiene una lista de todas las tareas.
    *   **Respuestas:**
        *   `200 OK`: Lista de objetos `Tarea`.

*   **`GET /tareas/{idTarea}`**
    *   **Descripción:** Obtiene una tarea específica por su ID.
    *   **Parámetros de Ruta:**
        *   `idTarea` (Long): El ID de la tarea.
    *   **Respuestas:**
        *   `200 OK`: Objeto `Tarea` si se encuentra.
        *   `404 Not Found`: Si la tarea no se encuentra.

*   **`POST /tareas`**
    *   **Descripción:** Crea una nueva tarea.
    *   **Cuerpo de la Solicitud:** Objeto `Tarea` (sin `id`).
    *   **Respuestas:**
        *   `200 OK`: La `Tarea` creada.

*   **`PUT /tareas/{id}`**
    *   **Descripción:** Actualiza una tarea existente.
    *   **Parámetros de Ruta:**
        *   `id` (Long): El ID de la tarea a actualizar.
    *   **Cuerpo de la Solicitud:** Objeto `Tarea` con los datos actualizados.
    *   **Respuestas:**
        *   `200 OK`: La `Tarea` actualizada.
        *   `404 Not Found`: Si la tarea no se encuentra.

*   **`DELETE /tareas/{id}`**
    *   **Descripción:** Elimina una tarea por su ID.
    *   **Parámetros de Ruta:**
        *   `id` (Long): El ID de la tarea a eliminar.
    *   **Respuestas:**
        *   `204 No Content`: Si la tarea fue eliminada exitosamente.
        *   `404 Not Found`: Si la tarea no se encuentra.

## Modelos de Datos

### Notificacion

Representa una notificación para un usuario.

| Campo       | Tipo          | Descripción                               |
| :---------- | :------------ | :---------------------------------------- |
| `id`        | `Long`        | Identificador único de la notificación.   |
| `idUsuario` | `Long`        | ID del usuario al que pertenece la notificación. |
| `mensaje`   | `String`      | Contenido del mensaje de la notificación. |
| `fecha`     | `LocalDateTime` | Fecha y hora en que se creó la notificación. |

### Recurso

Representa un recurso educativo.

| Campo         | Tipo     | Descripción                               |
| :------------ | :------- | :---------------------------------------- |
| `id`          | `Long`   | Identificador único del recurso.          |
| `titulo`      | `String` | Título del recurso.                       |
| `descripcion` | `String` | Descripción detallada del recurso.        |
| `materia`     | `String` | Materia a la que pertenece el recurso.    |

### Tarea

Representa una tarea asignada.

| Campo          | Tipo          | Descripción                               |
| :------------- | :------------ | :---------------------------------------- |
| `id`           | `Long`        | Identificador único de la tarea.          |
| `titulo`       | `String`      | Título de la tarea.                       |
| `descripcion`  | `String`      | Descripción detallada de la tarea.        |
| `fechaEntrega` | `LocalDateTime` | Fecha y hora límite para la entrega de la tarea. |
