from nodo import Nodo

class listaSimpleEnlazada():

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		return self.primero == None

	def agregar_inicio(self, dato):
		if self.vacia() == True:
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = Nodo(dato)
			aux.siguiente = self.primero
			self.primero = aux

	def agregar_ultimo(self, dato):
		if  self.vacia() == True:
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)

	def eliminar_inicio(self):
		self.primero = self.primero.siguiente

	def eliminar_ultimo(self):
		aux = self.primero
		while aux.siguiente != self.ultimo:
			aux = aux.siguiente
		aux.siguiente = None
		self.ultimo =  aux

	def imprimir(self):
		aux = self.primero
		while aux != None:
			print(aux.dato)
			aux = aux.siguiente