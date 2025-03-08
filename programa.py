tareas = []

print(tareas)

tarea1 = {
    "description": "tarea 1",
    "completed": False
}

tarea2 = {
    "description": "tarea 2",
    "completed": False
}

""" Agregar tareas """
print("Agregar")
tareas.append(tarea1)
tareas.append(tarea2)

""" Listar tareas """
print("Listar")
for tarea in tareas:
    print(f"{tarea['description']} {tarea['completed']}")

""" Completar tareas """
print("Completar")
tareas[1]['completed'] = True

""" Listar tareas """
print("Listar")
for tarea in tareas:
    print(f"{tarea['description']} {tarea['completed']}")

""" Eliminar tareas """
print("Eliminar")
tareas.pop(-1)

""" Listar tareas """
print("Listar")
for tarea in tareas:
    print(f"{tarea['description']} {tarea['completed']}")