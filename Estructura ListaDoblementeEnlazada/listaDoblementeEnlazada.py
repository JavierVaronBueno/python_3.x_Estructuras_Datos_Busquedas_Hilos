"""
ESTRUCTURA LISTA DOBLEMENTE ENLAZADA:
	Una lista doblemnete enlazada de nodos,
	donde cada nodo tiene un par de campos de
	enlace, uno al nodo siguiente y el otro al anterior.

	Caracteristicas:
		1- Recorre la estructura en smbos sentidos, de inicio a fin y de fin a inicio
		2- Borra mas simple los datos
		3- Estructura dinamica
"""

from nodo import Nodo
class listaDoblementeEnlazada():

	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.size = 0

	def vacia(self):
		return self.primero == None

	def agregar_final(self, dato):
		if  self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		#si no esta vacia, existe por lo menos un dato
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)
			self.ultimo.anterior = aux
		self.size += 1

	def agrgar_inicio(self, dato):
		if self.vacia() == True:
			self.primero =  self.ultimo = Nodo(dato)
		else:
			aux = Nodo(dato)
			aux.siguiente = self.primero
			self.primero = aux
		self.size += 1

	def eliminar_inicio(self):
		if self.vacia():
			print("Esta vacia la lista")
		elif self.primero.siguiente == None:
			self.primero = self.ultimo = None
			self.size = 0
		else:
			self.primero = self.primero.siguiente
			self.primero.anterior = None
			self.size -= 1

	def eliminar_final(self):
		if self.vacia():
			print("Esta vacia la lista")
		elif self.ultimo.anterior == None:
			self.ultimo = None
			self.size = 0
		else:
			self.ultimo =  self.ultimo.anterior
			self.ultimo.siguiente = None
			self.size -= 1


	def recorrer_inicio(self):
		aux = self.primero
		while aux:
			print(aux.dato)
			aux = aux.siguiente

	def recorrer_fin(self):
		aux = self.ultimo
		while aux:
			print(aux.dato)
			aux = aux.anterior

	def Size(self):
		return self.size
