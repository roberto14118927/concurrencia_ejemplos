import threading
import time

def primerHilo(argumento):
    time.sleep(2)
    print("Hola Hilo" + str(argumento))

print("Inicio del hilo")

threading.Thread(target=primerHilo(1)).start()
threading.Thread(target=primerHilo(2)).start()
threading.Thread(target=primerHilo(3)).start()