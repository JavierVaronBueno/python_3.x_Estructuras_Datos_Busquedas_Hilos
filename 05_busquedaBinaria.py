"""
METODO DE BUSQUEDA BINARIA:
Funcionamiento:
	1-
	2-
	3-
	4-
	5-
	6-
"""
def busquedaBinaria(dato):
	izquierda = 0
	derecha = len(lista) - 1
	while izquierda <= derecha:
		medio = (izquierda + derecha)//2#obtiene valor entero de la divicion
		if dato == lista[medio]:
			return medio
		elif dato < lista[medio]:
			derecha = medio - 1
		else:
			izquierda = medio + 1
	return None

def buscar(dato):
	if busquedaBinaria(dato) == None:
		return "El dato %d no se encontro."%(dato)
	else:
		return "El dato %d se encontro en el indice: %d"%(dato,busquedaBinaria(dato))

lista = [5,12,15,30,50,65,70,87,68,88,96]

for i in range(len(lista)):
	print("[%d]:-> [%d]"%(i,lista[i]))
	
print(buscar(12))