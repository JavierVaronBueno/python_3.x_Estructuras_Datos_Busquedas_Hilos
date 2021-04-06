import threading
import time
import datetime
import logging#indica que esta pasando en las sentecias de ejecucion

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(threadName)-s) %(message)s')

def consulta(id_persona):
	logging.info("Consultando para el id "+str(id_persona))
	time.sleep(2)
	return

def guardar(id_persona, data):
	logging.info("Guardando para el id "+str(id_persona)+" el data = \'"+data+"\'")
	time.sleep(5)
	return

tiempo_ini = datetime.datetime.now()

#declaracion de hilo de forma clasica
#name: declara el nombre d enuestro hilo; target:metodo o funcion que ejecutara; arg: argumentis del metoso si lo socilita en una tupla
t1 = threading.Thread(name="hilo_1", target = consulta, args=(1, ))
t2 =  threading.Thread(name="hilo_2",target = guardar, args=(1, "hola mundo"))

t1.start()
t2.start()

t1.join()
t2.join()
tiempo_fin = datetime.datetime.now()


print("Tiempo transcurrido "+str(tiempo_fin.second - tiempo_ini.second))
