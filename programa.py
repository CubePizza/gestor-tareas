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

def escoger_opcion():
    menu = """Gestor de tareas

1. Agregar tarea
2. Listar tareas
3. Completar tarea
4. Eliminar tarea
5. Salir

Escoger opcion: """
    opcion = int(input(menu))
    return opcion

    



""" Ejecucion del codigo """
while True:
    opcion = escoger_opcion()

    if opcion == 5:
        break
    elif opcion > 0 and opcion < 5:
        if opcion == 1:
            descripcion = input("Descripción de la tarea: ")

            if descripcion == "":
                print("Debe poner la descripcion")
            else:
                agregar_tarea(descripcion)

        elif opcion == 2:
            if len(tareas) > 0:
                listar_tareas()
            else:
                print("No hay tareas aun")
        
        elif opcion == 3:
            posicion = int(input("Numero de la tarea a eliminar: "))

            if posicion >= 0 and posicion < len(tareas):
                completar_tarea(posicion)
            else:
                print("Posición invalida")
        
        elif opcion == 4:
            posicion = int(input("Numero de la tarea a eliminar: "))

            if posicion >= 0 and posicion < len(tareas):
                eliminar_tarea(posicion)
            else:
                print("Posición invalida")
    else:
        print("Opcion invalida")