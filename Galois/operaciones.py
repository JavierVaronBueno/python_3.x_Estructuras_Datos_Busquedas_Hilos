from Aritmetica.Mostrovito import Algoritmo_Mostrovito
from Aritmetica.Tow_StepClassicMultiplication import Algoritmo_towStepClassicMultiplication


A_aux = '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
B_aux = '10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011000000000000000010000000000000000000001010000000000000000000000000000000000000'
M = 200
a=[]
b=[]

print("Tamaño de A: "+str(len(A_aux))+"\nTamaño de B:"+str(len(B_aux)))

#Convertimos la entrada en enteros
for i in range(M):
	a.append(int(A_aux[i]))
	b.append(int(B_aux[i]))



K=Algoritmo_Mostrovito(a, b, M)
P=Algoritmo_towStepClassicMultiplication(a, b, M)
print(Algoritmo_Mostrovito(a, b, M))
print(Algoritmo_towStepClassicMultiplication(a, b, M))

for i in range(M-1):
	if a[i] == b[i]:
		print(i)
		continue
	else:
		print("Error")
		break


