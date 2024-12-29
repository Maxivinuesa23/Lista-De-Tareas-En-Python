import view
    #!--------------------------------------------------Apartado para borrar tareas--------------------------------------------------

def borrar_tarea(lista_de_tareas):
    view.ver_tareas(lista_de_tareas)
    view.menu_ver_tarea_especifica(lista_de_tareas)
    print("Ingrese el número de tarea que desea borrar.")
    indice = (int(input("")) - 1)

    lista_de_tareas.pop(indice)