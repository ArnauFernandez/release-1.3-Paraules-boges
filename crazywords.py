import random

def crazywords(palabra):
    if len(palabra) <= 2:
        return palabra

    # Obtenemos la primera y última letra de la palabra
    primera_letra = palabra[0]
    ultima_letra = palabra[-1]

    # Convertimos las letras intermedias en una lista
    letras_medio = list(palabra[1:-1])

    # Aleatorizamos el orden de las letras intermedias
    random.shuffle(letras_medio)

    # Creamos la palabra "loca" uniendo todas las letras
    palabra_loca = primera_letra
    for letra in letras_medio:
        palabra_loca += letra
    palabra_loca += ultima_letra

    return palabra_loca
