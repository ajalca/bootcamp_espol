# 1. Escribir una función invertir_cadena(cadena) que invierta una cadena de texto.
# 2. Escribir una función contar_vocales(cadena) que cuente el número de vocales en una cadena de texto.
# 3. Guardar el código en un archivo manipulacion_cadenas.py.

def invertir_cadena(cadena):
    return cadena[::-1]
# Ejemplo
cadena_texto = "GANO SELECCION"
invertir_cadena = invertir_cadena(cadena_texto)
print(invertir_cadena)

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

# Ejemplo
texto = "GANO SELECCION"
vocales_contador = contar_vocales(texto)
print(vocales_contador)