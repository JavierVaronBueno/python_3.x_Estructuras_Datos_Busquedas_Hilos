
import threading
import time
import datetime
import logging
from Hilo1 import Hilo1
from Hilo2 import Hilo2


tiempo_ini = datetime.datetime.now()

#declaracion de hilo de forma clasica
#name: declara el nombre d enuestro hilo; target:metodo o funcion que ejecutara; arg: argumentis del metoso si lo socilita en una tupla
t1 = Hilo1("Hilo_1", 1, "")
t2 = Hilo2("Hilo_2", 1, "Hola mundo")

t1.start()
t2.start()

t1.join()
t2.join()

tiempo_fin = datetime.datetime.now()
print("Tiempo transcurrido "+str(tiempo_fin.second - tiempo_ini.second))