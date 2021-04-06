"""
METODO DE ORDENAMIENTO POR INSERCION:
Funcionamiento:
	1- Recorremos cada elemento de la lista
	2- Cada elemento de la lista se ordena si a su izquierda tiene un elemento mayor que el actual
	3- Si es correcto el paso anterior, se hace el intercambio de valores
	4-EL elemento se sigue recorriendo hacia la izquierda hasta que tenga un elemento menor o igual que el.
"""

lista = [5,1,8,12,10,3,1]
for i in range(1,len(lista)):
	aux = lista[i]
	izq = i -1 #0
	while  izq>= 0 and aux < lista[izq]:
		print(lista)
		print("Estoy en el indice i: %d ; izq: %d"%(i,izq))
		print("[i:%d] = %d es menor que [izq:%d] = %d"%(i,aux,izq, lista[izq]))
		lista[izq+1] = lista[izq]
		lista[izq] = aux
		izq -= 1

print(lista)