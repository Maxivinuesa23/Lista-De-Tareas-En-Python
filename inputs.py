from datetime import date
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

#!-------------------------------------------------- Funciones para controlar fechas--------------------------------------------------
def obtener_dia_vencimiento():
    dia = int(input("Ingrese el día de vencimiento\n"))

    while(dia < 1 or dia > 31):
        print("Ingrese un día valido.")
        dia = int(input("Ingrese el día de vencimiento\n"))

    return dia

def obtener_mes_vencimiento():
    mes = int(input("Ingrese el mes de vencimiento\n"))

    while (mes < 1 or mes > 12):
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