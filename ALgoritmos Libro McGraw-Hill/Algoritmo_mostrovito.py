import time

def suma(a,b):#XOR
	suma = (a+b)%2
	return suma

def multi(a,b):#AND
	mul = (a*b)%2
	return mul

def calculo_P(F, m):
	start_time = time.time()
	#Llenado de matriz P Relacionada con R del algoritmo Tow_Step
	P = [list(range(m)) for x in range(m-1)]
	"""
	#Llenado de matriz P Relacionada con R del algoritmo Tow_Step
	for j in range(0,m-1):#Fila
		P.append([0])
		for i in range(0,m-1):#Columna
			P[j].append(0)
	"""
	#Mapeo de los coeficientes de f(x)  en la primera fila de P
	for j in range(0,m):
		P[0][j] = F[j]

	#Construcción de P completa
	for i in range(1,m-1):
		for j in range(0,m):
			if j == 0:
				P[i][j] = P[i-1][m-1]
			else:	
				P[i][j] = suma(P[i-1][j-1],multi(P[i-1][m-1],P[0][j]))
		#print(P)
	print('Calculo [P] tiempo: %6.6f segundos'% ((time.time() - start_time)))
	return P

def calculo_Z(A,m,P):
	start_time = time.time()
	Z = []

	#Llenado de matriz Z con ceros
	for i in range(0,m):#Fila
		Z.append([0])
		for j in range(0,m-1):#Columna
			Z[i].append(0)
	#print(Z)
	
	
	#Mapeo de los coeficientes de a(x)  en la primera columna de Z
	for j in range(0,m):
		Z[j][0] = A[j]
	#print(Z)
	
	#Construcción de Z completa
	for j in range(1,m):#Columna
		for i in range(0,m):#Fila
			#si [u(i-j)<0] = 0
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
					#print("Z[",i,"][",j,"] := ","Z[",i,"][",j,"] + ","P[",(j-1-t),"][",i,"]*A[",(m-1-t),"]") 
					Z[i][j] = suma(Z[i][j], multi(P[j-1-t][i], A[m-1-t]))
				Z[i][j] = suma(Z[i][j], A[i-j])
				
	print('Calculo [Z] tiempo: %6.6f segundos'% ((time.time() - start_time)))	
	return Z

def multiplicacion_mostrovito(Z, B, M):
	start_time = time.time()
	C = []
	#Lenado de ceros de la lista C que sera el elemento resultante de la multiplicación
	for i in range(0, M):
		C.append(0)

	for i in range(0,M):#fila
		for j in range(0,M):#Columna
				C[i]=suma(C[i],multi(Z[i][j], B[j]))
	print('Calculo [C] tiempo: %6.6f segundos'% ((time.time() - start_time)))
	return C




A = [1, 1, 0, 0]
B = [1, 1, 0, 0]
M = 4
F = [1,1,0,0,1]
start_time = time.time()
P = calculo_P(F,M)
Z = calculo_Z(A,M,P)
C = multiplicacion_mostrovito(Z,B,M)
print('Resultado: %s \t %6.6f segundos'% (str(C),(time.time() - start_time)))
#print(P)
#print(Z)
#print(C)