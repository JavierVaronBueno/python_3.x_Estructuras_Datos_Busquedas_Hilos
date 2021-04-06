def one():
    return "Mi primer moemnto, junto a ti siempre sera el unico en esta vida, \n\tsiempre juntos en una vida llena de maravillas\n\t"
 
def two():
    return "Tengo atrapadas en mis dos retinas, \n\tLos moentos donde tomaste mi carne\n\tAbriste a mi tu cuerpo\n\tLlenaste de deseo mis sentidos\n\tDesataste un fuego que solo tu agua pudo apagar."
 
def three():
    return "Mi cama ahora es tu cama\n\tMi espacio ahora es tu espacio\n\tMis pensamientos estan invadidos de mis recuerdos de ti,\n\tEres quizas pequeña ante el universo\n\tPero enorme en mi corazon\n\tTe amo"
 
def four():
    return "En las noches claras,\n\tResuelvo el problema de la soledad del ser.\n\tInvito a mi luna y con el fuego de la pasion nos fundimos en uno\n\t uno mas o menos no importa\n\t Pues la soledad se resta, si la Luna brilla\n\t Su luz acobija mi alma y su tacto acaricia la siluta mi piel."
 
def five():
    return "Las notas de la musica, tienen hoy su encanto\n\tYa todo me suena a ti,\n\tA tus labios\n\ta tu sonrisa\n\ta tu tierna mirada en la mañana\n\ta la musica que hace tu vida tu existencia en mi."
 
def six():
    return "Inquieta mente que busca en lo oculto de la neblina\n\tNeblina de la montaña que desdibuja las formas de los arboles\n\tSususrro del viento frio que atemoriza las mañanas\n\tQuizas sea ya ña muerte o quizas sea el frio de la nueva llegada,\n\tMas se , que el sol no sale sin que acaricie el borde de la almuhada,\n\tDonde posas en letargo por una fina siesta\n\ta su vez profunda y estenuada,\n\tPues mataste con tu libido el deseo que tenia por ti\n\tSaciaste en las noches un cuerpo moribundo que estaba junto a ti\n\tY que al amanecer, el sol de tus ojos vuelve a revivir."
 
def seven():
    return "Dulce flor del campo, a ti las abejas polinizan\n\tY tu le concedes el dulce de tu nectar\n\tAcaso sabes de la belleza\n\tAcaso entiendes que eclipsas el sol con tu brillo\n\tSi fuera poco emanas el aroma\n\tUnico, deitante, afable que inundas las praderas\n\tCual carisma, inquieto\n\tDesbordas en ti tierna flor de la selva."
 
def eight():
    return "Azul y blanco es el cielo,\n\tEn ocaciones con tonos rojos y morados,\n\tSon unicos y varidos\n\tTan unicos como tu,\n\tTan variados como las formas que podria escribir en el cielo\n\tLo increible que ha sido tu amor."
 
def nine():
    return "Nueve años han pasado, quizas unos dias mas, quizas horas y minutos tambien\n\tPero el tiempo no significa nada,\n\tQuizas solo ha sido nueve segundos, un suspiro de una mariposa al nacer\n\tO el arrollo que corre en el manantial\n\tPero de lago estoy seguro que ni una vida de mil siglos y años,\n\tPodria quizas comprarce con nuestros nueve segundos."
 
def ten():
    return "Quizas en este momento estemos cansados\n\tLa monotonia consumiendonos de a poco,\n\tPero recuerda siempre estare junto a ti."
 
def numeros_de_amor(argument):
    #Diccionario
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
    }
    func = switcher.get(argument, lambda: "numero no valido")
    return func()

n = 's'

while (n != 'n'):
    num = int(input('Introduzca un numero de amor: '))
    print("\n",numeros_de_amor(num))
    print("Desea seguir? No:[n] - Si:[s]: ")
    n = input()
    print("\n")