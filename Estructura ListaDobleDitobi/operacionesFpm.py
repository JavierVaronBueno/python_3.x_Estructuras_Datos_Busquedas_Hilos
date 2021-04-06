from listaDobleDitobi import listaDobleDitobi

class operacionesFpm():
	def __init__(self):
		self.listaA = listaDobleDitobi()
		self.listaB = listaDobleDitobi()
		self.listaR = listaDobleDitobi()

	def sumaMod(self, listaA, listaB, m):
		self.listaA = listaA
		self.listaB = listaB
		A = listaA.primero
		B = listaB.primero
		sumaModular = 0
		for x in range(m):
			if x<1:
				sumaModular = (A.ditobi + B.ditobi)%2
			else:
				sumaModular = (A.ditobi + B.ditobi)%2
			A = A.siguiente
			B = B.siguiente
			self.listaR.agregar_final(sumaModular)