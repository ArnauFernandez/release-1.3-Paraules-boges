"""
Eric González, Izan Fernandez, Arnau Fernandez.
08/05/2024
M03 UF3
Descripció: Lliurament R3 ParaulesBoges

"""
import random

def crazywords(palabra):
    if len(palabra) <= 2:
        return palabra

    primera_letra = palabra[0]
    ultima_letra = palabra[-1]

    letras_medio = list(palabra[1:-1])

    random.shuffle(letras_medio)

    palabra_loca = primera_letra
    for letra in letras_medio:
        palabra_loca += letra
    palabra_loca += ultima_letra

    return palabra_loca
