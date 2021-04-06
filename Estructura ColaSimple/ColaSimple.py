"""
ESTRUCTURA DE DATOS COLA SIMPLE:
	Es una estructura de datos, caracterizada por ser una secuencia de elementos
	en la que la operación de inserción (push) se realiza por un extremo y la operacion
	de extracción (pop) por el otro. tambien se le llama estructura FIFO (First In First Out;
	Primero en Entrar, Primero en Salir), debido a que el primer elemento en entrar será tambien 
	el primero en salir.

	OPERACIONES:
		1.Insertar(pus)
		2.Eliminar(pop)
		3.Buscar
		4.Estado de la cola (empty)
		5.retornar el primer elememto
		6.retornar el tamaño de la cola
		7.ETC
"""		
class ColaSimple(object):
	"""dong fos ColaSimple"""
	def __init__(self):
		self.cola = []
		self.tam = 0

	def vacia(self):
		return len(self.cola) == 0

	def insertar(self, dato):
		self.cola += [dato]
		self.tam += 1

	def eliminar(self):
		if self.vacia():
			print("La cola esta vacia")
		else:
			self.cola = [self.cola[i] for i in range(1,self.tam)]
			self.tam -= 1

	def imprimir(self):
		n = self.tam - 1
		while n > -1:
			print("[%d]:-> %d"%(n,self.cola[n]))
			n -= 1

	def primerDato(self):
		if  self.vacia():
			print("Cola Vacía.")
		else:
			print("Primer dato: %d"%(self.cola[0]))
		