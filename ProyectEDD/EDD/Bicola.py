class Nodo:
    def __init__(self, dato):
        self.dato:str = dato
        self.siguiente = None
        self.anterior = None

    def imprimirNodo(self):
        return str(self.dato)


class Bicola:
    head = Nodo
    tail = Nodo

    def __init__(self):
        self.head = None
        self.head = None

    def agregarFrente(self, dato):
        n = Nodo(dato)
        if self.head is None:
            self.head = n
            self.tail = n
            return
        self.head.anterior = n
        n.siguiente = self.head
        self.head = n

    def agregarFinal(self, dato):
        n = Nodo(dato)
        if self.head is None:
            self.head = n
            self.tail = n
            return
        self.tail.siguiente = n
        n.anterior = self.tail
        self.tail = n

    def eliminarFrente(self):
        if self.head is None:
            return
        if self.head.siguiente is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.siguiente
        self.head.anterior = None

    def eliminarFinal(self):
        if self.head is None:
            return
        if self.head.siguiente is None:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.anterior
        self.tail.siguiente = None

    def imprimirBicola(self):
        h = self.head
        cadena = ""
        while h is not None:
            cadena += h.imprimirNodo()
            h = h.siguiente
        return cadena


if __name__ == '__main__':
    end = 0
    miBicola: Bicola = Bicola()
    while end == 0:
        print("quiere insertar al inicio o al final? [1. inicio/ 2. final]... (i para imprimir/ S salir)...")
        respuesta = input()
        if respuesta == "1":
            print("ingrese un dato...")
            n = Nodo(input())
            miBicola.agregarFrente(n)
            miBicola.imprimirBicola()
        if respuesta == "2":
            print("ingrese un dato...")
            n = Nodo(input())
            miBicola.agregarFinal(n)
            miBicola.imprimirBicola()
        if respuesta.upper() == "I":
            miBicola.imprimirBicola()
            print("desea eliminar un elemento? [s/n]...")
            r = input()
            if r.upper() == "S":
                print("Desea eliminar al frente o al final? [1. Frente/ 2. Final]...")
                ff = input()
                if ff == "1":
                    miBicola.eliminarFrente()
                    miBicola.imprimirBicola()
                if ff == "2":
                    miBicola.eliminarFinal()
                    miBicola.imprimirBicola()
        if respuesta.upper() == "S":
            miBicola.imprimirBicola()
            end = 1
