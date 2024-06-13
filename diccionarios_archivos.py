def leer_archivo(nombre_archivo):
    # iniciar un diccionario nuevo
    palabras = {}

    # abrir el archivo recibido
    with open(nombre_archivo, 'r') as archivo:

        # por cada linea en el archivo
        for linea in archivo.readlines():

            # removemos los espacios en blanco
            linea = linea.strip()

            # si la linea leida no esta en el diccionario, lo agregagamos y lo contamos una vez
            if linea not in palabras.keys():
                palabras[linea] = 1
            else:
                # si la line leida ya existe en el diccionario, contamos la aparacion de la line leida
                palabras[linea] += 1

    # retornar diccionario
    return palabras

def guardar_diccionario(diccionario, nombre_archivo):

    # convertimos el diccionario en una lista de texto conformado por
    # llave : valor\n
    lineas = ['%s : %d\n' % (llave, valor) for llave, valor in diccionario.items()]

    # abrimos el archivo de salida en modo escritura
    with open(nombre_archivo, 'w') as archivo:

        # guardamos cada item de lista lineas en el nuevo archivo
        archivo.writelines(lineas)


def main():
    palabras = leer_archivo('archivo.txt')
    guardar_diccionario(palabras, 'output.txt')

main()
