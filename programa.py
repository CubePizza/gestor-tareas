tareas = []

""" Funciones """
def agregar_tarea(descripcion):
    tareas.append({ 'descripcion': descripcion, 'completada': False })

def listar_tareas():
    for tarea in tareas:
        print(f"{tarea['descripcion']} {tarea['completada']}")

def completar_tarea(posicion):
    tareas[posicion]['completada'] = True

def eliminar_tarea(posicion):
    tareas.pop(posicion)


""" Ejecucion del codigo """
descripcion = "primera"

if descripcion == "":
    print("Debe poner la descripcion")
else:
    agregar_tarea(descripcion)

if len(tareas) > 0:
    listar_tareas()
else:
    print("No hay tareas aun")

posicion = 0

if posicion >= 0 and posicion < len(tareas):
    completar_tarea(posicion)
else:
    print("Posición invalida")

if len(tareas) > 0:
    listar_tareas()
else:
    print("No hay tareas aun")

posi = 0

if posi >= 0 and posi < len(tareas):
    eliminar_tarea(posi)
else:
    print("Posición invalida")

if len(tareas) > 0:
    listar_tareas()
else:
    print("No hay tareas aun")