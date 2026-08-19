import json
from pathlib import Path

RUTA_ARCHIVO = Path('tareas.json')

def cargar_tareas():
    try:
        with open(RUTA_ARCHIVO, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
            print("El archivo no existe... Creando archivo")
            with open(RUTA_ARCHIVO, 'w', encoding='utf-8') as archivo:
                json.dump([], archivo)
            datos = []
    return datos
    
def guardar_tareas(tareas: list[dict]):
    with open(RUTA_ARCHIVO, 'w', encoding = 'utf-8') as archivo:
        json.dump(tareas, archivo, ensure_ascii=False)