"""
ESTRUCTURA LISTA CIRCULAR SIMPLE:
	Es una lista en la que cada nodo tiene un enlace, similar al de las  listas enlazadas
	simples, excepto que el siguiente nodo del ultimo apunta al primero.

	Como en una lista enlazada simple, los nuevos nodos pueden ser solo eficientemente insertados
	después de uno que ya tengamos referenciado.

	Caracteristicas:
		- Permite acceso al primer nodo desde el puntero del ultimo nodo.
"""


from nodo import Nodo

class listaCircularSimple():
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		return self.primero == None

	def AgregarInicio(self, dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
			self.ultimo.siguiente = self.primero
		else:
			aux = self.primero
			self.primero = self.ultimo.siguiente = Nodo(dato)
			self.primero.siguiente = aux

	def AgregarFinal(self, dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
			self.ultimo.siguiente = self.primero
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)
			self.ultimo.siguiente = self.primero

	def RemoverInicio(self):
		if self.vacia():
			print("Lista vacia.")
		elif self.primero == self.ultimo:
			self.primero = self.ultimo = None
		else:
			self.primero = self.primero.siguiente
			self.ultimo.siguiente = self.primero

	def RemoverFinal(self):
		if self.vacia():
			print("Lista vacia.")
		elif self.primero == self.ultimo:
			self.primero = self.ultimo = None
		else:
			aux = self.primero
			while aux.siguiente != self.ultimo:
				aux = aux.siguiente
			aux.siguiente = self.primero
			self.ultimo = aux


	def Recorrer(self):
		aux = self.primero
		while aux:
			print(aux.dato)
			aux = aux.siguiente
			if aux == self.primero:
				break