
#!--------------------------------------------------Apartado para buscar tareas--------------------------------------------------
def buscar_tarea(lista_de_tareas):
    bandera = False
    print("Ingrese el titulo de la tarea que desea buscar")
    titulo_a_buscar = input("")
    
    for indice, tarea in enumerate(lista_de_tareas):
        if (titulo_a_buscar in tarea['Titulo']):
            bandera = True

            print("\n")
            print(f"[{indice + 1}] {tarea['Titulo']}")
            
        
    return bandera