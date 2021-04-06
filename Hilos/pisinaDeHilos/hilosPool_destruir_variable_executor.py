import time
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def saludo(a,b):
	time.sleep(1)
	logging.info(f'Proceso ejecutado variables a: {a}, b: {b} \n')
def hola():
	logging.info('Hola mundo')

if __name__ == '__main__':
	with ThreadPoolExecutor(max_workers=2) as executor:

		executor.submit(saludo, 1, 2)
		executor.submit(saludo, 3, 4)
		executor.submit(saludo, 5, 6)
		executor.submit(saludo, 7, 8)
		executor.submit(saludo, 9, 10)
		executor.submit(saludo, 11, 12)
		executor.submit(hola)#limito el ciclo de vida hasta esta linea