import emoji, view, search, delete, modify, inputs

#! --------------------------------------------------APARTADO PARA INGRESAR TAREAS A LA LISTA--------------------------------------------------
lista_de_tareas = []

def ingresar_tarea(titulo, descripcion, estado, dificultad, vencimiento):
    tarea: dict = {
        "Titulo": titulo,
        "Descripcion": descripcion,
        "Estado": estado,
        "Dificultad": dificultad,
        "Vencimiento": vencimiento
    }

    lista_de_tareas.append(tarea)
    



#! -------------------------------------------------- APARTADO MENU PRINCIPAL (main) --------------------------------------------------

while True:
    print("Bienvenido al menu de la Lista de tareas.")
    print("[1] Ver mis tareas.")
    print("[2] Buscar una tarea.")
    print("[3] Agregar una tarea.")
    print("[4] Modificar una tarea")
    print("[5] Borrar una tarea")
    print("[0] Salir.")
    opc = int(input(""))

    if (opc == 1):
        
        while True:
            print("¿Qué tareas deseas ver?")
            print("[1] Todas")
            print("[2] Pendientes")
            print("[3] En Curso")
            print("[4] Terminadas")
            print("[0] Volver")
            opc1 = int(input(""))

            if (opc1 == 1):
                print("Mostrando todas las tareas")
                view.ver_tareas(lista_de_tareas)
                view.menu_ver_tarea_especifica(lista_de_tareas)
                
            elif (opc1 == 2):
                print("Mostrando las tareas pendientes")
                view.ver_tareas_pendientes(lista_de_tareas)
                view.menu_ver_tarea_especifica(lista_de_tareas)

            elif (opc1 == 3):
                print("Mostrando las tareas en curso.")
                view.ver_tareas_en_curso(lista_de_tareas)
                view.menu_ver_tarea_especifica(lista_de_tareas)

            elif (opc1 == 4):
                print("Mostrando las tareas terminadas")
                view.ver_tareas_terminadas(lista_de_tareas)
                view.menu_ver_tarea_especifica(lista_de_tareas)

            else:
                break #! Vuelve al menu principal.
                



    elif (opc == 2):
        print("Usted selecciono BUSCAR UNA TAREA")
        print("--------------------------------------")
        bandera = search.buscar_tarea(lista_de_tareas)
        print("")

        if (bandera == True):
            view.menu_ver_tarea_especifica(lista_de_tareas)

        else:
            print("Lo sentimos, no pudimos encontrar esa tarea. Asegurate de escribir bien el titulo.")

        print("--------------------------------------")


    elif (opc == 3):
        print("Usted selecciono AGREGAR UNA TAREA") 
        titulo = inputs.ingresar_titulo()
        descripcion = inputs.ingresar_descripcion()
        estado = inputs.ingresar_estado()
        dificultad = emoji.traducir_dificultad_emoji(inputs.ingresar_dificultad())

        dia = inputs.obtener_dia_vencimiento()
        mes = inputs.obtener_mes_vencimiento()
        anio = inputs.obtener_anio_vencimiento()

        vencimiento = inputs.fecha_de_vencimiento(anio, mes, dia)

        ingresar_tarea(titulo, descripcion, estado, dificultad, vencimiento)

    elif (opc == 4):
        modify.modificar_tarea(lista_de_tareas)

    elif (opc == 5):
        delete.borrar_tarea(lista_de_tareas)

    elif (opc == 0):
        print("Gracias por utilizar la lista de tareas!")
        break

    else:
        print("Por favor, seleccione una opción valida.")



