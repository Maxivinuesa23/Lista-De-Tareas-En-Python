
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