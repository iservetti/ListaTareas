tareas = []
def agregar_tarea():
    tarea = input("Ingrese una tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")
def mostrar_tareas():
    print("Lista de tareas:")
    for tarea in tareas:
        print("- " + tarea)
def eliminar_tarea():
    mostrar_tareas()
    tarea = input("Ingrese la tarea a eliminar: ")
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea eliminada.")
    else:
        print("La tarea no está en la lista.")
while True:
    print("\nMenu:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
