"""
ESTRUCTURA DE DATO PILA:
	Una pila es una lista ordenada o estructura de datos en el que el modo de acceso 
	a sus elementos es de tipo 'LIFO' (Last In First Out, Ultimo En Entrar es el Primero en Salir),
	que permite almacenar datos.

	Para el manejo de los datos se cuenta con dos operaciones basicas:
		-Apilar(push): que coloca un objeto en la pila
		-Desapilar(pop): que retira el ultimo elemento apilado.

	OPERACIONES:
		-Crear: Se crea la pila vacía. (constructor)
		-Tamaño: Regresa el numero de los elementos de la pila (tam)
		-Apilar: Se añade un elemento a la pila.(push)
		-Desapilar: Se elimina el elemento ultimo en apilarse en la pila.(pop)
		-Cima:Devuelve el elemento que esta en la cima de la pila.(top o peek)
		-Vacía: Devuelve cierto si la pial esta vacía de lo contrario retorna falso.(empty)

Las pilas pueden ser de tamaño estatico y dinamico, se pueden implementar en listas, arreglos, colecciones
de datos o en listas enlazadas.
"""

class Pila():
	#Constructor
	def __init__(self,tam):
		self.lista = []
		self.tope = 0
		self.tam = tam #Tamaño de la pila 
	#Empty
	def vacia(self):
		if self.tope== 0:
			return True
		else:
			return False
	#Push
	def apilar(self, dato):
		if self.tope < self.tam:
			self.lista += [dato]#self.lista = self.lista + [dato]
			self.tope += 1#self.tope = self.tope + 1
		else:
			print("La pila esta llena")
			"""
			Pila dinamica
			self.tam += 1#self.tam = self.tam + 1
			self.lista +=[dato]#self.lista = self.lista + [dato]
			self.tope += 1#self.tope = self.tope + 1
			"""

	#Pop
	def desapilar(self):
		if self.vacia():
			print("La pila esta Vacia")
		else:
			self.tope -= 1# self.tope = self.tope - 1
			self.lista = [self.lista[x] for x in range(self.tope)]
			"""
			#La anterior linea es igua a esto:
			aux = []
			for x in range(self.tope):
				aux += [self.lista[x]]#aux = aux + [self.lista[x]]
			self.lista = aux
			"""
	#Show
	def imprimir(self):
		i = self.tope - 1
		while i > -1:
			print("[%d]:-> %d"%(i,self.lista[i]))
			i -= 1
	#Size
	def Tam(self):
		return self.tope
	#Top o peek
	def ultimoElemento(self):
		return self.lista[-1]