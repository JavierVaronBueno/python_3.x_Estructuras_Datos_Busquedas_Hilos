

def suma(a,b):#XOR
	suma = (a+b)%2
	return int(suma)

def multi(a,b):#AND
	mul = (a*b)%2
	return int(mul)
			

def poly_Multiplicacion(a,b,m):
	d = []
	for i in range(0, 2*m-2):
		d.append(0)
	
	for k in range(0,m-1):
		for i in range(0,k+1):
			if k == 0 and i == 1:
				continue
			d[k] = suma(d[k],multi(a[i],b[k-i]))


	for k in range(0,2*m-2):
		for i in range(k+1,2*m-2):
			d[k] = suma(d[k],multi(a[k-i+(m-1)],b[i-(m-1)]))

	return d

def reduccionMatrix_R(f,m):
	R =[]
	for j in range(0,m-1):#Fila
		R.append([])
		for i in range(0,m-2):#Columna
			R[j].append(0)
	for j in range(0,m-1):
		R[j][0] = f[j]
	
	for i in range(1,m-2):
		for j in range(0,m-1):
			if j == 0:
				R[j][i] = multi(R[m-1][i-1], R[j][0])
			else:
				R[j][i] = suma(R[j-1][i-1],multi(R[m-1, i-1],R[j][0]))
	return R


A = [0,1,1]#elemento F(2^3)
B = [1,0,1]#elemento F(2^3)
M = 3
F = [1,0,1,1]
D = poly_Multiplicacion(A,B,M)
R = reduccionMatrix_R(F,M)
print(D)
print(R)

C = []
for j in range(0,M-1):
	C.append(D[j])
for j in range(0,M-1):
	for i in range(0,M-2):
		C[j] = suma(C[j], multi(R[j][i],D[M+i]))

print(C)