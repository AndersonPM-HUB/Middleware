'''Clase padre'''

class Nodo:
    # lista de numeros guardados
    num = []
    # Diccionario  de vecinos
    vecinos = {}
    # variable para validar si el nodo ya respondio a la peticion
    bandera = 0

    def __init__(self,):
        pass

    def sumatoria(self):
        suma = 0
        for n in self.num:
            suma += n
        return suma


    def agregar_numero(self, n):
        self.num.append(n)


    def suma_vecinos(self, cantidad):
        total = self.sumatoria()
        total += cantidad
        return total