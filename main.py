import manipulacion_cadenas
import operaciones_listas
import diccionarios_archivos

import time

if __name__ == "__main__":
    lista1 = []
    lista2 = []
    #1. Lea una cadena de texto desde la entrada del usuario, invoque las funciones del archivo manipulación_cadenas.py y muestre los resultados.
    print("**************Grupo 3********************")
    print("***Vamos a trabajar con cadenas de texto***")
    x = input("Ingrese una cadena de texto: ")
    invertir = manipulacion_cadenas.invertir_cadena(x)
    contar = manipulacion_cadenas.contar_vocales(x)
    print("Su cadena invertida es: {}".format(invertir))
    print("Su cadena tiene {} vocales".format(contar))
    print("\n")
    print("***Vamos a trabajar con listas***")
    #2. Lea una lista de números desde la entrada del usuario, invoque las funciones del archivo operaciones_listas.py y muestre los resultados.
    for m in range(5):
        valor=int(input("Ingrese un valor entero:"))
        lista1.append(valor)
    operaciones_listas.sum_lista(lista1)

    for n in range(4):
        valor=int(input("Ingrese un valor entero:"))
        lista2.append(valor)
    operaciones_listas.mayor_elemento(lista2)
    print("\n")
    print("***Vamos a trabajar con archivos***")
    time.sleep(1)
    print("\n")
    print("...se está horneado el pastel...")
    #3. Lea un archivo de texto (por ejemplo, texto.txt), invoque las funciones del archivo diccionarios_archivos.py y guarde el diccionario resultante en un archivo `frecuencia_palabras.txt`.
    palabras = diccionarios_archivos.leer_archivo('archivo.txt')
    diccionarios_archivos.guardar_diccionario(palabras, 'frecuencia_palabras.txt')
    time.sleep(3)
    print("\n")
    print("Se ha generado automáticamente un archivo denominado frecuencia_palabras.txt")
    print("Apreciamos su tiempo. Bye")