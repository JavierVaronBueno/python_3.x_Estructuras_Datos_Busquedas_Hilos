from Pila import Pila

pila = Pila(8)

pila.apilar(23)
pila.apilar(90)
pila.apilar(45)
pila.apilar(24)
pila.apilar(2)
pila.apilar(45)
pila.apilar(24)
pila.apilar(2)

pila.desapilar()

print("Tamaño: %d"%(pila.Tam()))
print("Estao de la Pila: ",pila.vacia())
print("Ultimo Elemento: ",pila.ultimoElemento())

pila.imprimir()