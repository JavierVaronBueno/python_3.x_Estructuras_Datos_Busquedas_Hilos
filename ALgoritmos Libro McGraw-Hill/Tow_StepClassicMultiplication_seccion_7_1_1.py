
import time
global start_time
def suma(a,b):#XOR
	suma = (a+b)%2
	return suma

def multi(a,b):#AND
	mul = (a*b)%2
	return mul
			

def poly_Multiplicacion(a,b,m):
	start_time = time.time()
	d = []

	for i in range(0, 2*m-1):
		d.append(0)
	
	for k in range(0,m):
		if k == 0:
			#print("[0][0]=d[",k,"]+(a[0]b[0])") 
			d[0] = suma(d[0],multi(a[0],b[0]))
		else:
			for i in range(0,k+1):
				#print("[",k,"][",i,"]=d[",k,"]+(a[",i,"]b[",(k-i),"])")
				d[k] = suma(d[k],multi(a[i],b[k-i]))
	for k in range(m,2*m-1):
		for i in range(k,2*m-1):
			#print("[",k,"][",i,"]=d[",k,"]+(a[",k-i+(m-1),"]b[",i-(m-1),"])")
			d[k] = suma(d[k],multi(a[k-i+(m-1)],b[i-(m-1)]))
	print('Calculo [D] tiempo: %6.6f segundos'% ((time.time() - start_time)))	
	return d

			
def reduccionMatrix_R(f,m):
	start_time = time.time()
	#Llenado de matriz R con ceros
	R=[list(range(m-1)) for x in range(m)]
	#Llenado de matriz R con ceros
	"""
	#Llenado de matriz R con ceros
	for j in range(0,m):#Fila
		R.append([0])
		for i in range(0,m-2):#Columna
			R[j].append(0)
	"""		
	#print(R)
	#Mapeo de los coeficientes de f(x)  en la primera columna de R
	
	for j in range(0,m):
		R[j][0] = f[j]
	#print(R)
	#Construcción de R completa
	for i in range(1,m-1):
		for j in range(0,m):
			if j == 0:
				R[j][i] = multi(R[m-1][i-1], R[j][0])
			else:	
				R[j][i] = suma(R[j-1][i-1],multi(R[m-1][i-1],R[j][0]))
		#print(R)
	print('Calculo [R] tiempo: %6.6f segundos'% ((time.time() - start_time)))	
	return R

#Multiplicacion en dos pasos
def multiplicacion_Reduccion(submatriz_R, vector_D, M):
	start_time = time.time()
	C = []

	for j in range(0,M):
		C.append(vector_D[j])

	for j in range(0,M):
		for i in range(0,M-1):
				C[j]=suma(C[j],multi(submatriz_R[j][i], vector_D[M+i]))
	print('Calculo [C] tiempo: %6.6f segundos'% ((time.time() - start_time)))
	return C


A = [1, 1, 0, 0]
B = [1, 1, 0, 0]
M = 4
F = [1,1,0,0,1]
start_time = time.time()
D = poly_Multiplicacion(A,B,M)
R = reduccionMatrix_R(F,M)
C = multiplicacion_Reduccion(R,D,M)
print('Resultado: %s \t %6.6f segundos'% (str(C),(time.time() - start_time)))

#print("D:",D)
#print("R:",R)
#print("C:",C)