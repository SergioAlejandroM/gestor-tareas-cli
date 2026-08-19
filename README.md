# Gestor de Tareas CLI

Herramienta de línea de comandos para gestionar tareas pendientes, con persistencia local en JSON. Permite agregar, listar, completar, editar y eliminar tareas directamente desde la terminal.

## Tecnologías

- **Python 3.x**
- **argparse** — parseo de argumentos y subcomandos (librería estándar)
- **JSON** — persistencia de datos en disco

## Instalación

```bash
git clone https://github.com/tu-usuario/gestor-tareas-cli.git
cd gestor-tareas-cli
python main.py --help
```

No requiere dependencias externas — funciona solo con la librería estándar de Python.

## Uso

```bash
# Agregar una tarea
python main.py agregar "Comprar café"

# Listar todas las tareas
python main.py listar

# Marcar una tarea como completada
python main.py completar 1

# Editar el texto de una tarea
python main.py editar 1 "Comprar café con leche"

# Eliminar una tarea
python main.py eliminar 1
```

Al ejecutar el programa por primera vez, se crea automáticamente el archivo `tareas.json` donde se almacenan los datos.

## Decisiones técnicas

**Separación de responsabilidades.** El proyecto está dividido en tres módulos con una única responsabilidad cada uno: `almacenamiento.py` se encarga exclusivamente de leer y escribir el archivo JSON, `tareas.py` contiene la lógica de negocio (CRUD), y `main.py` maneja la interfaz de línea de comandos. Esta separación permite, por ejemplo, cambiar la persistencia de JSON a una base de datos como SQLite modificando únicamente `almacenamiento.py`, sin tocar el resto del código.

**IDs autoincrementales seguros.** En lugar de basar el nuevo ID en la posición o el último elemento de la lista, se calcula como el valor máximo de ID existente más uno (`max(ids, default=0) + 1`). Esto evita colisiones de ID incluso si se eliminan tareas intermedias, ya que no depende del orden ni de la longitud de la lista.

**Persistencia en JSON.** Se eligió JSON sobre CSV porque cada tarea es una estructura con múltiples campos (`id`, `texto`, `completada`), y JSON representa de forma nativa listas de objetos con esa estructura, sin necesidad de parseo manual adicional.

**Manejo explícito de errores.** Se evita el uso de `except` genérico en favor de capturar excepciones específicas (como `FileNotFoundError`), para no ocultar errores inesperados y facilitar el debugging.

**Construcción de listas nuevas en vez de mutación durante iteración.** Al eliminar una tarea, se construye una nueva lista filtrada (`[t for t in tareas if t["id"] != id_tarea]`) en lugar de modificar la lista mientras se recorre, evitando comportamientos inesperados al iterar y mutar simultáneamente.

## Posibles mejoras futuras

- Migrar la persistencia a SQLite
- Agregar fechas límite y prioridades a las tareas
- Suite de tests con `pytest`
- Type hints completos en todas las funciones
