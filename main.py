import manipulacion_cadenas

if __name__ == "__main__":
    x = input("Ingrese una cadena de texto: ")
    invertir = manipulacion_cadenas.invertir_cadena(x)
    contar = manipulacion_cadenas.contar_vocales(x)

    print("Su cadena invertida es: {}".format(invertir))
    print("Su cadena tiene {} vocales".format(contar))
