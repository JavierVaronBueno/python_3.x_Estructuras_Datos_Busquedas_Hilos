"""
NODO:
	en programación, concretamente en estructuras de datos,
	un nodo es uno de los elementos de una lista enlazada,
	de un arbol o de un grafo. Cada nodo será una estructura
	o registro que dispondrá de varios campos, y al menos uno
	de esos campos será un puntero o referencia de otro nodo,
	de forma que, conocido un nodo, apartir de esa referencia,
	erá posible en teoria tener acceso a otros nodos de la estructura.
"""

class Nodo():

	def __init__(self,dato,siguiente = None):
		self.dato = dato
		self.siguiente = siguiente

	def __str__(self):
		return str(self.dato)

def recorrer(nodo):
	while nodo != None:
		print(nodo.dato)
		nodo = nodo.siguiente

nodo4 = Nodo(23)
nodo3 = Nodo(43,nodo4)
nodo2 = Nodo(3,nodo3)
nodo1 = Nodo(4,nodo2)

recorrer(nodo1)
print(type(nodo1.dato))