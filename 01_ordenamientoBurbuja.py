"""
METODO DE ORDENAMIENTO BURBUJA:
	Revisa cada elemento de la lista con el siguiente elemento,
	intercambiandolos de pocision si estan en el orden equivocado.

	Ejemeplo:
	Entrada: 4,2,6,8,5,7

	Solucion:
		Recorrido [--,--] =  [4, 2, 6, 8, 5, 7]
		Recorrido [ 0 , 0 ] =  [4, 2, 6, 8, 5, 7]
		intercambio el valor  4  por el valor  2
		Recorrido [ 0 , 1 ] =  [2, 4, 6, 8, 5, 7]
		Recorrido [ 0 , 2 ] =  [2, 4, 6, 8, 5, 7]
		Recorrido [ 0 , 3 ] =  [2, 4, 6, 8, 5, 7]
		intercambio el valor  8  por el valor  5
		Recorrido [ 0 , 4 ] =  [2, 4, 6, 5, 8, 7]
		intercambio el valor  8  por el valor  7
		Recorrido [ 1 , 0 ] =  [2, 4, 6, 5, 7, 8]
		Recorrido [ 1 , 1 ] =  [2, 4, 6, 5, 7, 8]
		Recorrido [ 1 , 2 ] =  [2, 4, 6, 5, 7, 8]
		intercambio el valor  6  por el valor  5
		Recorrido [ 1 , 3 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 1 , 4 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 2 , 0 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 2 , 1 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 2 , 2 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 2 , 3 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 2 , 4 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 3 , 0 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 3 , 1 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 3 , 2 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 3 , 3 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 3 , 4 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 4 , 0 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 4 , 1 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 4 , 2 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 4 , 3 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 4 , 4 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 5 , 0 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 5 , 1 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 5 , 2 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 5 , 3 ] =  [2, 4, 5, 6, 7, 8]
		Recorrido [ 5 , 4 ] =  [2, 4, 5, 6, 7, 8]
	
	Salida: 2,4,5,6,7,8

"""

lista = [4,2,6,8,5,7]
print("Recorrido [--,--] = ",lista)
#loop para comparar elemento por cada elemento de la lista
for i in range(len(lista)):
	#loop para selecionar cada elemento de la lista y compararlo con el elemento del primer loop
	for x in range(len(lista)-1):
		print("Recorrido [",i,",",x,"] = ",lista)
		if lista[x]>lista[x+1]:
			print("intercambio el valor ",lista[x]," por el valor ",lista[x+1])
			aux = lista[x]
			lista[x]=lista[x+1]
			lista[x+1] = aux
	
print("\n lista ordenada: ",lista)		


