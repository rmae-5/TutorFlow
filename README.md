# Proyecto TutorFlow

## Introducción

TutorFlow es una organización privada en el rubro de la Tecnología Educativa, dedicada a ofrecer soluciones innovadoras para mejorar la experiencia de aprendizaje y gestión académica. Este proyecto integra un servidor backend desarrollado con Spring Boot y un cliente de línea de comandos en Python, diseñados para trabajar en conjunto y proporcionar una plataforma robusta para la gestión educativa.

## Servicios Web Ofrecidos

La plataforma TutorFlow ofrece los siguientes servicios web principales:

### 1. Notificaciones y Recordatorios
Permite la gestión y envío de notificaciones a los usuarios, asegurando que estén siempre informados sobre eventos importantes, fechas límite y actualizaciones relevantes.

### 2. Recursos Académicos Compartidos
Facilita la carga, organización y acceso a una amplia variedad de recursos educativos, como documentos, enlaces y materiales de estudio, clasificados por materia para una fácil búsqueda.

### 3. Gestión de Tareas y Evaluaciones
Proporciona herramientas para la creación, asignación y seguimiento de tareas y evaluaciones, incluyendo fechas de entrega y descripciones detalladas, lo que ayuda a estudiantes y educadores a mantener un control efectivo del progreso académico.

## Estructura del Proyecto

El proyecto TutorFlow se compone de dos módulos principales:

### `servidor-springboot/`
Este directorio contiene el backend de la aplicación, desarrollado con Spring Boot. Es el corazón de la API REST que expone los servicios de Notificaciones, Recursos y Tareas.

*   **Tecnología:** Spring Boot (Java)
*   **Base de Datos:** PostgreSQL (configurada a través de `postgres.yml` para Docker Compose)
*   **Documentación de la API:** Ver `servidor-springboot/API_DOCUMENTATION.md` para detalles sobre los endpoints y modelos de datos.

### `cliente-python/`
Este directorio contiene un cliente de línea de comandos desarrollado en Python. Este cliente interactúa con la API REST del servidor Spring Boot, permitiendo a los usuarios acceder y gestionar los servicios de TutorFlow desde la terminal.

*   **Tecnología:** Python
*   **Funcionalidades:** Listar notificaciones, listar notificaciones por usuario, listar recursos (con filtro por materia), listar tareas, y obtener una tarea por ID.
*   **Documentación del Cliente:** Ver `cliente-python/CLIENT_DOCUMENTATION.md` para instrucciones de uso y detalles de las funciones.

## Cómo Empezar

Para configurar y ejecutar el proyecto, consulte los archivos `README.md` específicos dentro de cada subdirectorio (`servidor-springboot/README.md` y `cliente-python/README.md`) para obtener instrucciones detalladas.
