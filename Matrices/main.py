"""
ESTRUCTURA DE MATRIZ

MATRIZ 5X5
			Columnas
			0 1 2 3 4
			--------- 
		0|	1 2 3 4 5 
		1|	8 1 2 8 9 
Filas	2|	9 7 0 4 1
		3|	5 5 4 3 2
		4|	7 5 3 2 1


 
"""
"""
matriz = [[15,24,34,45,75],[58,34,55,62,89],[23,41,65,29,45],[3,5,45,21,3],[8,56,34,2,9]]

#Imprimir matriz
for i in matriz:
	print(i)

#Generador de matrices

matriz = []
filas = 5
columnas = 5
print("matriz de %dX%d"%(filas,columnas))
for x in range(filas):
	matriz.append([])
	for y in range(columnas):
		matriz[x].append(None)

for m in matriz:
	print(m)

#generador de matriz por compresion

matrix =[list(range(10)) for x in range(10)]

for x in matrix:
	print(x)

R =[]
for j in range(0,5-1):
	R.append([])
	for i in range(0,5-2):
		R[j].append(0)

for x in R:
	print(x)

s = [[1,2],[3,4]]

print(s[0][0])

for x in range(1,1):
	print("hola")
"""
"""
m=4
R=[]
for j in range(0,m-1):#Fila
	for i in range(0,m-2):#Columna
		R.append([0])



print(R)
"""
"""
l = [[1,8,9],[8,0,4]]
print(l[0][2])
a=[]


R=[]
m=5
for j in range(0,m):#Fila
	R.append([0])
	for i in range(0,m-2):#Columna
		R[j].append(0)	
print(R)

m=4
Z = [list(range(m)) for x in range(m)]
print(Z)
"""