from listaDobleDitobi import listaDobleDitobi
from operacionesFpm import operacionesFpm

operar = operacionesFpm()
listaA = listaDobleDitobi()
listaB = listaDobleDitobi()
listaR = listaDobleDitobi()

listaA.agregar_final(0)
listaA.agregar_final(0)
listaA.agregar_final(0)
listaA.agregar_final(0)
listaA.agregar_final(1)

listaB.agregar_final(1)
listaB.agregar_final(0)
listaB.agregar_final(0)
listaB.agregar_final(0)
listaB.agregar_final(0)


print("A:")
listaA.recorrer_inicio()
print("B:")
listaB.recorrer_inicio()
print("R:")
operar.sumaMod(listaA, listaB, 5)
listaR = operar.listaR
listaR.recorrer_inicio()
print("Traducido:")
listaR.recorrer_fin_traducido(5)





