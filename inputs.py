
#! --------------------------------------------------FUNCIONES PARA INGRESAR VALORES--------------------------------------------------

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