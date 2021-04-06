"""
METODO ORDENAMIENTO POR SELECCION:
	Es un algoritmo que consiste en ordenar los elementos de manera acedendente o descendente
	PASOS:
	-Busca el dato mas pequeño de la lista
	-Intercambiarlo por el actual
	-Seguir buscando el dato mas pequeño de la lista
	-Intercambiarlo por el actual
	-Esto se repetira sucecivamente
	Ejemplo:
	Entrada: [4, 2, 6, 8, 5, 7, 0]

	Solucion:
	[0, 2, 6, 8, 5, 7, 4]
	[0, 2, 6, 8, 5, 7, 4]
	[0, 2, 4, 8, 5, 7, 6]
	[0, 2, 4, 5, 8, 7, 6]
	[0, 2, 4, 5, 6, 7, 8]

	Salida: [0, 2, 4, 5, 6, 7, 8]
"""

lista = [4,2,6,8,5,7,0]

#Loop para recorrer los elementos de la lista
for i in range(len(lista)):
	minimo = i
	#loop para buscar el menor elemento d ela lista
	for x in range(i,len(lista)):
		if lista[x]< lista[minimo]:
			minimo = x
	#intercambio del menor valor en sus pocision correcta
	aux = lista[i]
	lista[i] = lista[minimo]
	lista[minimo] = aux
	print(lista)
	