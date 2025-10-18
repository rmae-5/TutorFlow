import requests
import json
from datetime import datetime


API_BASE_URL = "http://localhost:8100/api"  # Cambia el puerto si es necesario
HEADERS = {"Content-Type": "application/json"}


def crear_tarea(titulo: str, descripcion: str, fecha_entrega_iso: str):
    """
    fecha_entrega_iso: 'YYYY-MM-DDTHH:MM:SS' (ISO-8601).
    """
    url = f"{API_BASE_URL}/tareas"
    payload = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fechaEntrega": fecha_entrega_iso
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    _print_response(r)


def actualizar_tarea(id_tarea: int, titulo: str | None = None,
                     descripcion: str | None = None, fecha_entrega_iso: str | None = None):
    url = f"{API_BASE_URL}/tareas/{id_tarea}"
    body = {}
    if titulo is not None: body["titulo"] = titulo
    if descripcion is not None: body["descripcion"] = descripcion
    if fecha_entrega_iso is not None: body["fechaEntrega"] = fecha_entrega_iso
    if not body:
        print("Nada que actualizar en Tarea.")
        return
    r = requests.put(url, headers=HEADERS, json=body)
    _print_response(r)


def eliminar_tarea(id_tarea: int):
    url = f"{API_BASE_URL}/tareas/{id_tarea}"
    r = requests.delete(url, headers=HEADERS)
    _print_response(r)


def crear_recurso(titulo: str, descripcion: str, materia: str):
    url = f"{API_BASE_URL}/recursos"
    payload = {
        "titulo": titulo,
        "descripcion": descripcion,
        "materia": materia
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    _print_response(r)


def actualizar_recurso(id_recurso: int, titulo: str | None = None,
                       descripcion: str | None = None, materia: str | None = None):
    url = f"{API_BASE_URL}/recursos/{id_recurso}"
    body = {}
    if titulo is not None: body["titulo"] = titulo
    if descripcion is not None: body["descripcion"] = descripcion
    if materia is not None: body["materia"] = materia
    if not body:
        print("Nada que actualizar en Recurso.")
        return
    r = requests.put(url, headers=HEADERS, json=body)
    _print_response(r)


def eliminar_recurso(id_recurso: int):
    url = f"{API_BASE_URL}/recursos/{id_recurso}"
    r = requests.delete(url, headers=HEADERS)
    _print_response(r)


def actualizar_notificacion(id_notificacion: int, id_usuario: int | None = None,
                            mensaje: str | None = None, fecha_iso: str | None = None):
    """
    Actualiza campos provistos; los que vengan None no se tocan (si tu backend requiere todos,
    pásalos todos).
    """
    url = f"{API_BASE_URL}/notificaciones/{id_notificacion}"
    # arma el body solo con lo que envías
    body = {}
    if id_usuario is not None: body["idUsuario"] = int(id_usuario)
    if mensaje is not None: body["mensaje"] = mensaje
    if fecha_iso is not None: body["fecha"] = fecha_iso
    if not body:
        print("Nada que actualizar. Pasa al menos un campo.")
        return
    r = requests.put(url, headers=HEADERS, json=body)
    _print_response(r)

def eliminar_notificacion(id_notificacion: int):
    url = f"{API_BASE_URL}/notificaciones/{id_notificacion}"
    r = requests.delete(url, headers=HEADERS)
    _print_response(r)


def crear_notificacion(id_usuario: int, mensaje: str, fecha_iso: str | None = None):
    """
    Crea una notificación.
    fecha_iso: ISO-8601 (ej: '2025-10-18T12:30:00'), si None se usa ahora().
    """
    url = f"{API_BASE_URL}/notificaciones"
    payload = {
        "idUsuario": int(id_usuario),
        "mensaje": mensaje,
        "fecha": fecha_iso or datetime.now().isoformat(timespec="seconds")
    }
    r = requests.post(url, headers=HEADERS, json=payload)
    _print_response(r)


def _print_response(r):
    print("Código de estado:", r.status_code)
    try:
        print("Respuesta:", json.dumps(r.json(), indent=4, ensure_ascii=False))
    except ValueError:
        print("Respuesta (texto):", r.text)


def listar_notificaciones():
    print("\nListando todas las notificaciones...")
    r = requests.get(f"{API_BASE_URL}/notificaciones")
    print("Código de estado:", r.status_code)
    print("Respuesta:", json.dumps(r.json(), indent=4, ensure_ascii=False))


def listar_notificaciones_usuario(id_usuario):
    print(f"\nListando notificaciones del usuario {id_usuario}...")
    r = requests.get(f"{API_BASE_URL}/notificaciones/{id_usuario}")
    print("Código de estado:", r.status_code)
    print("Respuesta:", json.dumps(r.json(), indent=4, ensure_ascii=False))


def listar_recursos(materia=None):
    url = f"{API_BASE_URL}/recursos"
    params = {"materia": materia} if materia else {}
    print("\nListando recursos académicos...")
    r = requests.get(url, params=params)
    print("Código de estado:", r.status_code)
    print("Respuesta:", json.dumps(r.json(), indent=4, ensure_ascii=False))


def listar_tareas():
    print("\nListando todas las tareas...")
    r = requests.get(f"{API_BASE_URL}/tareas")
    print("Código de estado:", r.status_code)
    print("Respuesta:", json.dumps(r.json(), indent=4, ensure_ascii=False))


def obtener_tarea(id_tarea):
    print(f"\nConsultando tarea con ID {id_tarea}...")
    r = requests.get(f"{API_BASE_URL}/tareas/{id_tarea}")
    print("Código de estado:", r.status_code)
    print("Respuesta:", json.dumps(r.json(), indent=4, ensure_ascii=False))


def menu():
    while True:
        print("\n========== CLIENTE TUTORFLOW ==========")
        print("1. Listar todas las notificaciones")
        print("2. Listar notificaciones por usuario")
        print("3. Listar recursos académicos")
        print("4. Listar tareas")
        print("5. Consultar tarea por ID")
        print("6. Crear notificación")
        print("7. Actualizar notificación")
        print("8. Eliminar notificación")
        print("9. Crear recurso")
        print("10. Actualizar recurso")
        print("11. Eliminar recurso")
        print("12. Crear tarea")
        print("13. Actualizar tarea")
        print("14. Eliminar tarea")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_notificaciones()
        elif opcion == "2":
            idu = input("Ingrese ID de usuario: ")
            listar_notificaciones_usuario(idu)
        elif opcion == "3":
            mat = input("Filtrar por materia (opcional): ").strip()
            listar_recursos(mat if mat else None)
        elif opcion == "4":
            listar_tareas()
        elif opcion == "5":
            idt = input("Ingrese ID de tarea: ")
            obtener_tarea(idt)
        elif opcion == "6":
            idu = input("ID usuario: ")
            msg = input("Mensaje: ")
            fecha = input("Fecha ISO (enter para ahora): ").strip() or None
            crear_notificacion(idu, msg, fecha)
        elif opcion == "7":
            idi = int(input("ID notificación a actualizar: "))
            idu = input("Nuevo ID usuario (enter para omitir): ").strip()
            msg = input("Nuevo mensaje (enter para omitir): ").strip()
            fecha = input("Nueva fecha ISO (enter para omitir): ").strip()
            actualizar_notificacion(
                idi,
                int(idu) if idu else None,
                msg if msg else None,
                fecha if fecha else None
            )
        elif opcion == "8":
            idi = int(input("ID notificación a eliminar: "))
            eliminar_notificacion(idi)
        elif opcion == "9":
            t = input("Título: ")
            d = input("Descripción: ")
            m = input("Materia: ")
            crear_recurso(t, d, m)
        elif opcion == "10":
            idi = int(input("ID recurso a actualizar: "))
            t = input("Título (enter para omitir): ").strip()
            d = input("Descripción (enter para omitir): ").strip()
            m = input("Materia (enter para omitir): ").strip()
            actualizar_recurso(
                idi,
                t if t else None,
                d if d else None,
                m if m else None
            )
        elif opcion == "11":
            idi = int(input("ID recurso a eliminar: "))
            eliminar_recurso(idi)
        elif opcion == "12":
            t = input("Título: ")
            d = input("Descripción: ")
            f = input("Fecha entrega ISO (p.ej. 2025-10-25T23:59:00): ")
            crear_tarea(t, d, f)
        elif opcion == "13":
            idi = int(input("ID tarea a actualizar: "))
            t = input("Título (enter para omitir): ").strip()
            d = input("Descripción (enter para omitir): ").strip()
            f = input("Fecha entrega ISO (enter para omitir): ").strip()
            actualizar_tarea(
                idi,
                t if t else None,
                d if d else None,
                f if f else None
            )
        elif opcion == "14":
            idi = int(input("ID tarea a eliminar: "))
            eliminar_tarea(idi)
        elif opcion == "0":
            print("Saliendo del cliente...")
            break
        else:
            print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    print(f"Iniciando cliente TutorFlow - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        menu()
    except Exception as e:
        print("Error en la comunicación con el servidor:", e)