import inputs
import view
import emoji
#! -------------------------------------------------- APARTADO PARA MODIFICAR TAREAS----------------------------------------------------------------

def modificar_tarea(lista_de_tareas):
    if not lista_de_tareas:
        print("No hay tareas en la lista para modificar!")  #! Controlamos que la lista tenga tareas dentro.
        return 


    print("---------------TAREAS------------------")
    view.ver_tareas(lista_de_tareas) #!Mostramos las tareas para que el usuario pueda seleccionar cual quiere modificar.
    print("---------------------------------------")

    try:
        indice = (int(input("Ingrese el numero de la tarea a modificar\n"))   - 1)

        if indice < 0 or indice >= len(lista_de_tareas):
            print("Indice fuera de rango. Intente nuevamente")
            return

        tarea = lista_de_tareas[indice]
        while True:
            print("------------------------------------")
            print(f"Modificando la tarea N° {indice + 1}")
            print("------------------------------------")
            print("") 

            print("¿Qué valor desea modificar?")
            print("[1] Titulo")
            print("[2] Descripción")
            print("[3] Estado")
            print("[4] Dificultad")
            print("[5] Vencimiento")
            print("[0] Volver al menu principal.")
            valor = int(input(""))

            if (valor == 1):
                tarea['Titulo'] = inputs.ingresar_titulo()
                print("Tarea modificada con exito!")
            elif (valor == 2):
                tarea['Descripcion'] = inputs.ingresar_descripcion()
                print("Tarea modificada con exito!")
            elif (valor == 3):
                tarea['Estado'] = inputs.tipos_de_estado()
                print("Tarea modificada con exito!")
            elif (valor == 4):
                tarea['Dificultad'] = emoji.traducir_dificultad_emoji(inputs.ingresar_dificultad())
                print("Tarea modificada con exito!")
            elif (valor == 5):
                dia = inputs.obtener_dia_vencimiento()
                mes = inputs.obtener_mes_vencimiento()
                anio = inputs.obtener_anio_vencimiento()
                tarea['Vencimiento'] = inputs.fecha_de_vencimiento(anio, mes, dia)
                print("Tarea modificada con exito!")
            elif (valor == 0):
                break
            else:
                print("Ingrese una opción valida.")

    except ValueError:
        print("El valor que ingreso es invalido. Asegurese de ingresar un número.") 