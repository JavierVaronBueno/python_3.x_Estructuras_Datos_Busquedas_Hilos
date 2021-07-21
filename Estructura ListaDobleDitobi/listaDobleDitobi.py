from nodoDitobi import NodoDitobi
class listaDobleDitobi():

	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.size = 0

	def vacia(self):
		return self.primero == None

	def agregar_final(self, dato):
		if  self.vacia():
			self.primero = self.ultimo = NodoDitobi(dato)
		#si no esta vacia, existe por lo menos un dato
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = NodoDitobi(dato)
			self.ultimo.anterior = aux
		self.size += 1

	def agrgar_inicio(self, dato):
		if self.vacia() == True:
			self.primero =  self.ultimo = NodoDitobi(dato)
		else:
			aux = NodoDitobi(dato)
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
			print(aux.ditobi)
			aux = aux.siguiente

	def recorrer_fin(self):
		aux = self.ultimo
		while aux:
			print(aux.ditobi)
			aux = aux.anterior
			
	"""
		Impresión en forma polinomial de los elementos de la lista,
		descripción de los elementos en el campo de extensión
	"""
	def recorrer_fin_traducido(self, m):
		aux = self.primero
		cont = m
		while aux:
			if aux.ditobi == 1:
				if cont > 1:
					print("&alpha;^"+str(cont-1))
				else:
					print(1)
			
			aux = aux.siguiente
			cont -=1

	def Size(self):
		return self.size
