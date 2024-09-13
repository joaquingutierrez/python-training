def codificacion_mensaje_p1 (msg):
    vocales = "aeiouAEIOU"
    mensaje_codificado = ""
    imagen_especular = ""
    for c in msg:
        esVocal = c in vocales
        if esVocal:
            mensaje_codificado = mensaje_codificado + imagen_especular + c
            imagen_especular = ""
        else:
            imagen_especular = c + imagen_especular

    mensaje_codificado = mensaje_codificado + imagen_especular
    return mensaje_codificado

def codificacion_mensaje_p2 (msg):
    mensaje_codificado = ""
    cant_caracteres = cant_caracteres_del_mensaje(msg)
    cant_ciclos = cant_caracteres // 2
    for i in range(0, cant_ciclos):
        mensaje_codificado = mensaje_codificado + msg[i] + msg[cant_caracteres - i - 1]
    if (cant_caracteres % 2 == 1): # Solo si la cantidad de caracteres es impar
        mensaje_codificado = mensaje_codificado + msg[int(cant_caracteres / 2 + 0.5 - 1)]
    return mensaje_codificado

def decodificacion_mensaje_p2 (msg):
    mensaje_codificado = ""
    cant_caracteres = cant_caracteres_del_mensaje(msg)
    cant_ciclos = cant_caracteres // 2
    for i in range(0, cant_ciclos):
        mensaje_codificado = mensaje_codificado + msg[i * 2]
    if (cant_caracteres % 2 == 1): # Solo si la cantidad de caracteres es impar
        mensaje_codificado = mensaje_codificado + msg[cant_caracteres-1]
    for i in range(cant_ciclos, 0, -1):
        mensaje_codificado = mensaje_codificado + msg[i * 2 - 1]
    return mensaje_codificado

def cant_caracteres_del_mensaje (msg):
    cant = 0
    for c in msg:
        cant = cant + 1
    return cant

def codificar_mensaje ():
    msg = input("Introduzca el mensaje a cifrar: ")
    msg_p1 = codificacion_mensaje_p1(msg)
    msg_p2 = codificacion_mensaje_p2(msg_p1)
    print(msg + " => " + msg_p2)

def descifar_mensaje ():
    msg = input("Introduzca el mensaje a decifrar: ")
    msg ="E. .n.ualn cnhuag aMda rle"
    msg_p1 = decodificacion_mensaje_p2(msg)
    msg_p2 = codificacion_mensaje_p1(msg_p1)
    print(msg + " => " + msg_p2)

codificar_mensaje()
descifar_mensaje()


#Tengo un problema con este ejemplo: 
#E. .n.ualn cnhuag aMda rle => En un lugar de la Mancha...
#El resultado que obtengo es diferente. El resultado es: En un lugal dera Mancha...
# Pero si le agrego un espacio de la siguiente manera al mensaje cifrado, me queda bien.
#E. .n.ualn cnhuag aMda  rle => En un lugar de la Mancha...
#No se si es algo que estoy haciendo mal o simplemente era que le faltaba un espacio al mensaje cifrado: