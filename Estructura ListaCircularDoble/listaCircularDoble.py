from nodo import Nodo

class listaCircularDoble():

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		return self.primero == None

	def __unirNodos(self):
		self.primero.anterior = self.ultimo
		self.ultimo.siguiente = self.primero

	def agregarInicio(self, dato):
		if sel.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = Nodo(dato)
			aux.siguiente = self.primero
			self.primero.anterior = aux
			self.primero = aux
		self.__unirNodos()

	def agregarFinal(self, dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)
			self.ultimo.anterior = aux
		self.__unirNodos()

	def recorrerInicio(self):
		aux = self.primero
		while aux:
			print(aux.dato)
			aux = aux.siguiente
			aux = aux.siguiente
			if  aux == self.primero:
				break

	def recorrerFin(self):
		aux = self.ultimo
		while aux:
			print(aux.dato)
			aux = aux.anterior

