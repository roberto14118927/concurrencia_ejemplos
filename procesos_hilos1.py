# import para importar librerias a utilizar en el programa 
import threading
import time
import os
import multiprocessing

# Decalara una variable llamada num y su tipo es entero
num = 4

# Creacion de las funciones 
# void o function => def en python 

def tarea1(): 
    # Imprimir resultado
    print("PID: %s, Nombre proceso: %s, Nombre Thread: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name
    ))
    time.sleep(1) #Para dar un tiempo de reposo


def tarea2(): 
    # Imprimir resultado
    print("PID: %s, Nombre proceso: %s, Nombre Thread: %s" % (
        os.getpid(),
        multiprocessing.current_process().name,
        threading.current_thread().name
    ))
    conta = 0
    while conta < 100000000:
        conta += 1

start_time = time.time()
for _ in range(num):
    tarea2()
end_time = time.time()

print("Tiempo Final Serial:", end_time - start_time)

# utilizando threads
start_timec = time.time()
threads = [threading.Thread(target=tarea2) for _ in range(num)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
end_timec = time.time()
concurrente = end_timec - start_timec
print("Tiempo Final Concurrente:", concurrente)


# utilizando procesos
start_timep = time.time()
processes = [multiprocessing.Process(target=tarea2) for _ in range(num)]
[process.start() for process in processes]
[process.join() for process in processes]
end_timep = time.time()

paralelo = end_timep - start_timep

print("Tiempo Final Paralelo:", paralelo)


print("Tiempo concurrente vs paralelo:", paralelo - concurrente )

