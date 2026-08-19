import argparse
from almacenamiento import cargar_tareas
from tareas import agregar_tarea, listar_tareas, completar_tarea, eliminar_tarea, editar_tarea

parser = argparse.ArgumentParser(description="Gestor de tareas")

subparsers = parser.add_subparsers(dest="comando")

parser_agregar = subparsers.add_parser("agregar")
parser_agregar.add_argument("texto")

parser_listar = subparsers.add_parser("listar")

parser_completar = subparsers.add_parser("completar")
parser_completar.add_argument("id", type=int)

parser_eliminar = subparsers.add_parser("eliminar")
parser_eliminar.add_argument("id", type=int)

parser_editar = subparsers.add_parser("editar")
parser_editar.add_argument("id", type=int)
parser_editar.add_argument("texto")

def main():
    args = parser.parse_args()
    tareas = cargar_tareas()

    if args.comando == "agregar":
        agregar_tarea(tareas, args.texto)
    elif args.comando == "listar":
        listar_tareas(tareas)
    elif args.comando == "completar":
        completar_tarea(tareas, args.id)
    elif args.comando == "eliminar":
        eliminar_tarea(tareas, args.id)
    elif args.comando == "editar":
        editar_tarea(tareas, args.id, args.texto)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
