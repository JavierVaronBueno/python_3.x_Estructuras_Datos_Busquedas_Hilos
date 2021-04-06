"""
Recursividad: 
	Es una funcion que se llama a si misma
	Ejemplo:
		-Factorial de 4:
			4! = 4*3*2*1 = 24
"""

def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(4))

"""
n=4						1ra llmada = 24
return 4 * factorial(3)

n=3						2da llamada = 6
return 3 * factorial(2)

n=2						3ra llamada = 2
return 2 * factorial(1)
	 	
n=1						
return 1
"""