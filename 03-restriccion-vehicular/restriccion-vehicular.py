digitos = {"lunes": (3, 4, 5, 6), "martes": (7, 8, 9, 0), "miercoles": (1, 2, 3, 4), "jueves":(5, 6, 7, 8), "vienes": (9, 0, 1, 2)}

def estaConRestriccion (digitos, dia, patente):
    digito_patente = int(patente[-2])
    digitos_con_resticcion = digitos[dia]
    return digito_patente in digitos_con_resticcion

def diasConRestriccion(digitos, patente):
    digito_patente = int(patente[-2])
    dias = []
    for dia, digitos_con_resticcion in digitos.items():
        if digito_patente in digitos_con_resticcion:
            dias.append(dia)
    return dias

def diasSinRestriccion (digitos, patente):
    digito_patente = int(patente[-2])
    dias = set()
    for dia, digitos_con_resticcion in digitos.items():
        if digito_patente not in digitos_con_resticcion:
            dias.add(dia)
    return dias

estaConRestriccion_BBDT35 = estaConRestriccion(digitos, "lunes", "BBDT35")
print(estaConRestriccion_BBDT35)
diasConRestriccion_BBDT35 = diasConRestriccion(digitos, "BBDT35")
print(diasConRestriccion_BBDT35)
diasSinRestriccion_BBDT35 = diasSinRestriccion(digitos, "BBDT35")
print(diasSinRestriccion_BBDT35)