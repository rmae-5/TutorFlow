import requests
import json
from datetime import datetime

API_BASE_URL = "http://localhost:8100/api"  # Cambia el puerto si es necesario
HEADERS = {"Content-Type": "application/json"}


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