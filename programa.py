import json

class GestorTareas():
    def __init__(self, archivo="tareas.json"):
        self.archivo = archivo
        self.tareas = self.cargar_tareas()
    
    def guardar_tareas(self):
        with open(self.archivo, "w") as f:
            json.dump(self.tareas, f, indent=4)

    def cargar_tareas(self):
        try:
            with open(self.archivo, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def agregar_tarea(self, descripcion):
        if not descripcion:
            print("Debe poner la descripcion")
            return
        
        self.tareas.append({ 'descripcion': descripcion, 'completada': False })
        self.guardar_tareas()
        print(f"Tarea '{descripcion}' agregada")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas aun")
            return
        
        for i, tarea in enumerate(self.tareas, 1):
            estado = "✅" if tarea['completada'] else "❌"
            print(f"{i}. {tarea['descripcion']} {estado}")

    def completar_tarea(self, posicion):
        if 0 < posicion <= len(self.tareas):
            self.tareas[posicion - 1]['completada'] = True
            self.guardar_tareas()
            print(f"Tarea '{self.tareas[posicion - 1]['descripcion']}' completada.")
        else:
            print("Posición invalida")
    
    def eliminar_tarea(self, posicion):
        if 0 < posicion <= len(self.tareas):
            tarea = self.tareas.pop(posicion - 1)
            print(f"Tarea '{tarea['descripcion']}' eliminada.")
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

gestor = GestorTareas()
while True:
    opcion = escoger_opcion()

    if opcion == 5:
        break
    elif 1 <= opcion < 5:
        if opcion == 1:
            tarea = input("Descripción de la tarea: ")
            gestor.agregar_tarea(tarea)
            gestor.listar_tareas()

        elif opcion == 2:
            gestor.listar_tareas()
        
        elif opcion == 3:
            posicion = int(input("Numero de la tarea a completar: "))
            gestor.completar_tarea(posicion)
            gestor.listar_tareas()

        else:
            posicion = int(input("Numero de la tarea a eliminar: "))
            gestor.eliminar_tarea(posicion)
            gestor.listar_tareas()
    else:
        print("Opcion invalida")