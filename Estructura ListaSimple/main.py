from listaSimpleEnlazada import listaSimpleEnlazada

lista = listaSimpleEnlazada()

lista.agregar_ultimo(12)
lista.agregar_ultimo(2)
lista.agregar_ultimo(1)
lista.agregar_ultimo(3)
lista.agregar_ultimo(34)
lista.agregar_ultimo(8)

lista.eliminar_ultimo()
lista.eliminar_ultimo()
lista.eliminar_ultimo()
lista.eliminar_ultimo()
lista.eliminar_ultimo()

lista.agregar_inicio(45)
lista.agregar_inicio(90)

lista.eliminar_inicio()

print(lista.primero)
print(lista.ultimo)

lista.imprimir()
