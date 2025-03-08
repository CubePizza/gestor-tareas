tareas = []

""" Funciones """
def agregar_tarea(descripcion):
    if not descripcion:
        print("Debe poner la descripcion")
        return
    
    tareas.append({ 'descripcion': descripcion, 'completada': False })
    print(f"Tarea '{descripcion}' agregada")

def listar_tareas():
    if not tareas:
        print("No hay tareas aun")
        return
    
    for tarea in tareas:
        estado = ""
        if tarea['completada']:
            estado = "✅"
        else:
            estado = "❌"

        print(f"{tarea['descripcion']} {estado}")

def completar_tarea(posicion):
    if 0 < posicion <= len(tareas):
        tareas[posicion - 1]['completada'] = True
    else:
        print("Posición invalida")
    

def eliminar_tarea(posicion):
    if 0 < posicion <= len(tareas):
        tareas.pop(posicion - 1)
    else:
        print("Posición invalida")
    

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
            agregar_tarea(descripcion)

        elif opcion == 2:
            listar_tareas()
        
        elif opcion == 3:
            posicion = int(input("Numero de la tarea a completar: "))
            completar_tarea(posicion)

            
        
        elif opcion == 4:
            posicion = int(input("Numero de la tarea a eliminar: "))
            eliminar_tarea(posicion)
    else:
        print("Opcion invalida")