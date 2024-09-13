personas_cromosomas = {"Pedro": "00000101010101010101", "Juan": "00101010101101110111", "Diego": "00100010010000001001"}

def encontrarSospechoso (DNA):
    count = 0
    countMax = 0
    i = 0
    sospechoso = ""
    porcentaje = 0
    for persona, cromosoma in personas_cromosomas.items():
        for c in DNA:
            if c == cromosoma[i]:
                count = count + 1
            i = i + 1
        if count >= countMax:
            countMax = count
            sospechoso = persona
        count = 0
        i = 0
        porcentaje = countMax * 100 / 20
    return (sospechoso, porcentaje)

def introducirSeceunciaDNA ():
    DNA = input("Por favor, introduzca la secuencia a analizar: ")
    sospechoso, porcentaje = encontrarSospechoso(DNA)
    print("El culpable es: ", sospechoso, "con un porcentaje de", porcentaje, "%")

introducirSeceunciaDNA()