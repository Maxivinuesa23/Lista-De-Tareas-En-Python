from datetime import date


#!--------------------------------------------------FUNCIONES PARA INGRESAR VALORES--------------------------------------------------

def ingresar_titulo():
    titulo = input("Por favor, ingrese el titulo. El mismo no puede ser vacio\n")

    while titulo == "":
        print("Por favor, ingresa un titulo valido. (No vacio)\n")
        titulo = input("Por favor, ingrese el titulo. El mismo no puede ser vacio\n")

    return titulo

def ingresar_descripcion():
    descripcion = input("Por favor, ingrese la descripción de la tarea.")
    return descripcion

def ingresar_estado():
    estado = "Pendiente"
    return estado

def tipos_de_estado():
    print("¿En que estado se encuentra su tarea?")
    print("---------------")
    print("[1] Pendiente")
    print("[2] En proceso")
    print("[3] Terminado")
    print("---------------")
    estado = int(input(""))

    if ((estado != 1) and (estado != 2) and (estado != 3)):
        print("Por favor, ingrese un estado valido.")
        tipos_de_estado()
    
    if(estado == 1):
        estado = "Pendiente"
    elif (estado == 2):
        estado = "En proceso"
    elif (estado == 3):
        estado = "Terminado"
    
    return estado


def ingresar_dificultad():
    print("Ingrese la dificultad de la tarea")
    print("[F] -> Facil")
    print("[M] -> Medio")
    print("[D] -> Dificil")
    estado = input("")

    estado = estado.upper()

    if ((estado != "F") and (estado != "M") and (estado != "D") and (estado == "")):
        print("Por favor, ingrese una dificultad valida.")
        ingresar_dificultad()

    return estado




#!-------------------------------------------------- Funciones para controlar fechas--------------------------------------------------
def obtener_dia_vencimiento():
    dia = int(input("Ingrese el día de vencimiento\n"))

    while(dia < 1 and dia > 31):
        print("Ingrese un día valido.")
        dia = int(input("Ingrese el día de vencimiento\n"))

    return dia

def obtener_mes_vencimiento():
    mes = int(input("Ingrese el mes de vencimiento\n"))

    while (mes < 1 and mes > 12):
        print("Ingrese un mes valido.")
        mes = int(input("Ingrese el mes de vencimiento\n"))
    
    return mes

def obtener_anio_vencimiento():
    anio = int(input("Ingrese el año de vencimiento\n"))

    while (anio < 2024):
        print("Ingrese un año valido")
        anio = int(input("Ingrese el año de vencimiento\n"))
    
    return anio

def fecha_de_vencimiento(dia, mes, anio):
    vencimiento = date(dia, mes, anio)
    return vencimiento

#! --------------------------------------------------APARTADO PARA COLOCAR EMOJIS--------------------------------------------------

def traducir_dificultad_emoji(dificultad):
    if (dificultad == 'F'):
        dificultad = "⭐"
    elif (dificultad == 'M'):
        dificultad = "⭐⭐"
    elif (dificultad == 'D'):
        dificultad = "⭐⭐⭐"
    
    return dificultad

def traducir_dificultad_string(dificultad):
    if (dificultad == "⭐"):
        dificultad = "F"
    elif (dificultad == "⭐⭐"):
        dificultad = "M"
    elif (dificultad == "⭐⭐⭐"):
        dificultad = "D"
    
    return dificultad


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
    




#! -------------------------------------------------- APARTADO PARA MOSTRAR TAREAS EN LA LISTA --------------------------------------------------
def ver_tareas():
    for indice, tarea in enumerate(lista_de_tareas):
        print("--------------------------------------")
        print(f"Tarea N° {indice + 1}")
        print(f"Titulo: {tarea['Titulo']}")
        print("--------------------------------------")
        print("\n")


def ver_tareas_pendientes():
    for indice, tarea in enumerate(lista_de_tareas):
        if (tarea['Estado'] == 'Pendiente'):
            print("--------------------------------------")
            print(f"Tarea N° {indice + 1}")
            print(f"Titulo: {tarea['Titulo']}")
            print("--------------------------------------")
            print("\n")

def ver_tareas_en_curso():
    for indice, tarea in enumerate(lista_de_tareas):
        if (tarea['Estado'] == 'En Curso'):
            print("--------------------------------------")
            print(f"Tarea N° {indice + 1}")
            print(f"Titulo: {tarea['Titulo']}")
            print("--------------------------------------")
            print("\n")

def ver_tareas_terminadas():
    for indice, tarea in enumerate(lista_de_tareas):
        if (tarea['Estado'] == 'Terminado'):
            print("--------------------------------------")
            print(f"Tarea N° {indice + 1}")
            print(f"Titulo: {tarea['Titulo']}")
            print("--------------------------------------")
            print("\n")

def ver_tarea_especifica(indice):

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

def menu_ver_tarea_especifica():
    print("¿Desea ver los detalles de alguna tarea?")
    print("Introduce el número para verla o 0 para volver")
    indice = int(input(""))

    if (indice == 0):
        return
    else:
        ver_tarea_especifica(indice)

#! -------------------------------------------------- APARTADO PARA MODIFICAR TAREAS----------------------------------------------------------------

def modificar_tarea():
    if not lista_de_tareas:
        print("No hay tareas en la lista para modificar!")  #! Controlamos que la lista tenga tareas dentro.
        return 


    print("---------------TAREAS------------------")
    ver_tareas() #!Mostramos las tareas para que el usuario pueda seleccionar cual quiere modificar.
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
                tarea['Titulo'] = ingresar_titulo()
                print("Tarea modificada con exito!")
            elif (valor == 2):
                tarea['Descripcion'] = ingresar_descripcion()
                print("Tarea modificada con exito!")
            elif (valor == 3):
                tarea['Estado'] = tipos_de_estado()
                print("Tarea modificada con exito!")
            elif (valor == 4):
                tarea['Dificultad'] = traducir_dificultad_emoji(ingresar_dificultad())
                print("Tarea modificada con exito!")
            elif (valor == 5):
                dia = obtener_dia_vencimiento()
                mes = obtener_mes_vencimiento()
                anio = obtener_anio_vencimiento()
                tarea['Vencimiento'] = fecha_de_vencimiento(anio, mes, dia)
                print("Tarea modificada con exito!")
            elif (valor == 0):
                break
            else:
                print("Ingrese una opción valida.")

    except ValueError:
        print("El valor que ingreso es invalido. Asegurese de ingresar un número.") 

    
#!--------------------------------------------------Apartado para buscar tareas--------------------------------------------------
def buscar_tarea():
    bandera = False
    print("Ingrese el titulo de la tarea que desea buscar")
    titulo_a_buscar = input("")
    
    for indice, tarea in enumerate(lista_de_tareas):
        if (titulo_a_buscar in tarea['Titulo']):
            bandera = True

            print("\n")
            print(f"[{indice + 1}] {tarea['Titulo']}")
            
        
    return bandera




#! -------------------------------------------------- APARTADO MENU PRINCIPAL (main) --------------------------------------------------

while True:
    print("Bienvenido al menu de la Lista de tareas.")
    print("[1] Ver mis tareas.")
    print("[2] Buscar una tarea.")
    print("[3] Agregar una tarea.")
    print("[4] Modificar una tarea")
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
                ver_tareas()
                menu_ver_tarea_especifica()
                
            elif (opc1 == 2):
                print("Mostrando las tareas pendientes")
                ver_tareas_pendientes()
                menu_ver_tarea_especifica()

            elif (opc1 == 3):
                print("Mostrando las tareas en curso.")
                ver_tareas_en_curso()
                menu_ver_tarea_especifica()

            elif (opc1 == 4):
                print("Mostrando las tareas terminadas")
                ver_tareas_terminadas()
                menu_ver_tarea_especifica()

            else:
                break #! Vuelve al menu principal.
                



    elif (opc == 2):
        print("Usted selecciono BUSCAR UNA TAREA")
        print("--------------------------------------")
        bandera = buscar_tarea()
        print("")

        if (bandera == True):
            menu_ver_tarea_especifica()

        else:
            print("Lo sentimos, no pudimos encontrar esa tarea. Asegurate de escribir bien el titulo.")

        print("--------------------------------------")


    elif (opc == 3):
        print("Usted selecciono AGREGAR UNA TAREA") 
        titulo = ingresar_titulo()
        descripcion = ingresar_descripcion()
        estado = ingresar_estado()
        dificultad = traducir_dificultad_emoji(ingresar_dificultad())

        dia = obtener_dia_vencimiento()
        mes = obtener_mes_vencimiento()
        anio = obtener_anio_vencimiento()

        vencimiento = fecha_de_vencimiento(anio, mes, dia)

        ingresar_tarea(titulo, descripcion, estado, dificultad, vencimiento)

    elif (opc == 4):
        modificar_tarea()

    elif (opc == 0):
        print("Gracias por utilizar la lista de tareas!")
        break

    else:
        print("Por favor, seleccione una opción valida.")



