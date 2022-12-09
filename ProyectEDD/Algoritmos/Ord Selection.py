import random


def ordenamientoSeleccion(datos, tamañoO):
    contador = 0
    comparaciones = 0
    intercambios = 0
    i = 0
    j = 0
    tamaño = tamañoO
    minimo = 0
    aux = 0
    while i < tamaño:
        contador = contador + 1
        minimo = i
        j = i + 1
        while j < tamaño:
            comparaciones = comparaciones + 1
            if datos[j] < datos[minimo]:
                minimo = j
            intercambios = intercambios + 1
            j = j + 1
        aux = datos[i]
        datos[i] = datos[minimo]
        datos[minimo] = aux
        i = i + 1
    for item in datos:
        print(str(item))


if __name__ == "__main__":
    datos = []
    tamaño = int(input())
    j = 0
    while j < tamaño:
        datos.append(random.randint(0, 100))
        j = j + 1
    cadena = ""
    for item in datos:
        cadena += str(item) + ", "
    print(cadena)
    ordenamientoSeleccion(datos, tamaño)
