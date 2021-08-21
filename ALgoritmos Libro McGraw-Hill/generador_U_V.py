import math


def generador_U(m):
    regla =0
    #  length t
    t = int(math.ceil(math.log(m-1, 2)))+1
    #print(f'm = {m} ; t = {t-1}')
    #  a finite sequence of integers U
    lista_u = []
    for i in range(0,t):
        # print(f'i = {i}')
        if i == 0:
            lista_u.append(1)
        elif i == t-1:
            print("Primera regla")
            lista_u.append(lista_u[t-2]+lista_u[t-3])
            print(lista_u)            
            regla = 1
            print(generador_V(regla,m))
            if lista_u[t-2]+lista_u[t-3] != m-1:
                print("segunda regla")
                regla = 2
                
                lista_u = []
                for j in range(0,t):

                    if j == 0:
                        lista_u.append(1)
                    elif j == 2:
                        lista_u.append(lista_u[0] + lista_u[1])
                    else:
                        lista_u.append(2*lista_u[-1])
                print(generador_V(regla,m))
        else:
            lista_u.append(2*lista_u[i-1])
    
    print(lista_u)
    return lista_u

def generador_V(regla,m):
    	#  length t
    t = int(math.ceil(math.log(m-1, 2)))+1
    print(f'm = {m} ; e = {m-1} ; t = {t-1}')
    #  a finite sequence of integers U
    lista_v = []
    if regla == 1:
        for i in range(0,t):
            # print(f'i = {i}')
            if i == 0:
                lista_v.append([])
            elif i == t-1:
                lista_v.append([i-2,i-1])
            else:
                lista_v.append([i-1, i-1])
        #print(lista_u)
    if regla == 2:
        for i in range(0,t):
            # print(f'i = {i}')
            if i == 0:
                lista_v.append([])
            elif i == 2:
                lista_v.append([0,1])
            else:
                lista_v.append([i-1, i-1])
    return lista_v


M=8
U = generador_U(M)


