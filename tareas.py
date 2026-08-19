from almacenamiento import guardar_tareas

def agregar_tarea(tareas: list, texto: str) -> list:

    nuevo_id = max((t["id"] for t in tareas), default = 0) + 1

    tarea = {
            "id": nuevo_id,
            "texto": texto,
            "completada": False
        }

    tareas.append(tarea)

    guardar_tareas(tareas)

    return tareas

def completar_tarea(tareas: list, id_tarea: int) -> list:

    encontrada = False

    for tarea in tareas:
        if(tarea["id"] == id_tarea):
            encontrada = True
            tarea["completada"] = True
            print("Se marco como completada la tarea")
            break

    if not encontrada:
        print("No se encontro la tarea")

    guardar_tareas(tareas)

    return tareas

def editar_tarea(tareas: list, id_tarea: int, nuevo_texto: str) -> list:
    encontrada = False
    
    for tarea in tareas:
        if(tarea["id"] == id_tarea):
            encontrada = True
            tarea["texto"] = nuevo_texto
            print("Se actualizo el contenido de la tarea")
            break
    
    if not encontrada:
        print("No se encontro la tarea")
    
    guardar_tareas(tareas)
    
    return tareas

def eliminar_tarea(tareas: list, id_tarea: int) -> list:

    existe = any(t["id"] == id_tarea for t in tareas)
    
    if not existe:
        print("No se encontró la tarea")
        return tareas
    
    tareas = [t for t in tareas if t["id"] != id_tarea]
    guardar_tareas(tareas)
    return tareas

def listar_tareas(tareas: list):
    for t in tareas:
        print(f"[{t['id']}] {'✔' if t['completada'] else '✗'} {t['texto']}")