"""
----------------------------------------------------------------------------------------------------------
			Algoritmo Mostrovito 
----------------------------------------------------------------------------------------------------------

ENTRADAS:
		A, B, M, F
SALIDA:
		C
"""
from Polinomios.Irreducibles import PolinomioBinario

def suma(a,b):#función XOR
	suma = (a+b)%2
	return suma

def multi(a,b):#función AND
	mul = (a*b)%2
	return mul

def calculo_P(F, m):
	
	#Llenado de matriz P 
	P = [list(range(m)) for x in range(m-1)]
	
	#Mapeo de los coeficientes de la función irreducible [f(x)]  en la primera fila de P
	for j in range(0,m):
		P[0][j] = F[j]

	#Construcción de P completa
	for i in range(1,m-1):
		for j in range(0,m):
			if j == 0:
				P[i][j] = P[i-1][m-1]
			else:	
				P[i][j] = suma(P[i-1][j-1],multi(P[i-1][m-1],P[0][j]))
	return P

def calculo_Z(A,m,P):
	
	Z = []

	#Llenado de matriz Z con ceros
	for i in range(0,m):#Fila
		Z.append([0])
		for j in range(0,m-1):#Columna
			Z[i].append(0)
	
	#Mapeo de los coeficientes de a(x)  en la primera columna de Z
	for j in range(0,m):
		Z[j][0] = A[j]

	#Construcción de Z completa
	for j in range(1,m):#Columna
		for i in range(0,m):#Fila
			if i < j:
				#cuando t = 0 
				if j == 1:
					#print("Z[",i,"][",j,"] := ","Z[",i,"][",j,"] + ","P[",(j-1),"][",i,"]*A[",(m-1),"]")
					Z[i][j] = suma(Z[i][j], multi(P[j-1][i], A[m-1]))
				#cuando t > 0 
				else:
					for t in range(0,j):
						#print("Z[",i,"][",j,"] := ","Z[",i,"][",j,"] + ","P[",(j-1-t),"][",i,"]*A[",(m-1-t),"]") 
						Z[i][j] = suma(Z[i][j], multi(P[j-1-t][i], A[m-1-t]))
						
			else:
				for t in range(0,j):
					Z[i][j] = suma(Z[i][j], multi(P[j-1-t][i], A[m-1-t]))
				Z[i][j] = suma(Z[i][j], A[i-j])
	return Z

def multiplicacion_mostrovito(Z, B, M):
	C = []
	#Lenado de ceros de la lista C que sera el elemento resultante de la multiplicación
	for i in range(0, M):
		C.append(0)

	for i in range(0,M):#fila
		for j in range(0,M):#Columna
				C[i]=suma(C[i],multi(Z[i][j], B[j]))
	return C

def Algoritmo_Mostrovito(A, B, M):
	P = calculo_P(PolinomioBinario(M), M)
	Z = calculo_Z(A, M, P)
	return multiplicacion_mostrovito(Z, B, M)



