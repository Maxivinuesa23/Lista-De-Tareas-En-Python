
#! -------------------------------------------------- APARTADO PARA MOSTRAR TAREAS EN LA LISTA --------------------------------------------------
def ver_tareas(lista_de_tareas):
    for indice, tarea in enumerate(lista_de_tareas):
        print("--------------------------------------")
        print(f"Tarea N° {indice + 1}")
        print(f"Titulo: {tarea['Titulo']}")
        print("--------------------------------------")
        print("\n")


def ver_tareas_pendientes(lista_de_tareas):
    for indice, tarea in enumerate(lista_de_tareas):
        if (tarea['Estado'] == 'Pendiente'):
            print("--------------------------------------")
            print(f"Tarea N° {indice + 1}")
            print(f"Titulo: {tarea['Titulo']}")
            print("--------------------------------------")
            print("\n")

def ver_tareas_en_curso(lista_de_tareas):
    for indice, tarea in enumerate(lista_de_tareas):
        if (tarea['Estado'] == 'En Curso'):
            print("--------------------------------------")
            print(f"Tarea N° {indice + 1}")
            print(f"Titulo: {tarea['Titulo']}")
            print("--------------------------------------")
            print("\n")

def ver_tareas_terminadas(lista_de_tareas):
    for indice, tarea in enumerate(lista_de_tareas):
        if (tarea['Estado'] == 'Terminado'):
            print("--------------------------------------")
            print(f"Tarea N° {indice + 1}")
            print(f"Titulo: {tarea['Titulo']}")
            print("--------------------------------------")
            print("\n")

#! ------------------------------------------------------------------------------------
def menu_ver_tarea_especifica(lista_de_tareas):
    print("¿Desea ver los detalles de alguna tarea?")
    print("Introduce el número para verla o 0 para volver")
    indice = int(input(""))

    if (indice == 0):
        return
    else:
        ver_tarea_especifica(indice, lista_de_tareas)



def ver_tarea_especifica(indice, lista_de_tareas):

    indice = indice - 1
    try:
        
        if indice < 0 or indice >= len(lista_de_tareas):
            print("Indice ingresado no valido. Intente nuevamente")
            return
        
        tarea = lista_de_tareas[indice]

        print("--------------------------------------")
        print(f"Tarea N° {indice + 1}")
        print(f"Titulo: {tarea['Titulo']}")
        print(f"Descripcion: {tarea['Descripcion']}")
        print(f"Estado: {tarea['Estado']}")
        print(f"Dificultad: {tarea['Dificultad']}")
        print(f"Vencimiento: {tarea['Vencimiento']}")
        print("--------------------------------------")
        print("\n")

    except ValueError:
        print("Ingrese un valor valido.")