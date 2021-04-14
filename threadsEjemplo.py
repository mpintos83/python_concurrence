import threading
import time

def tarea():
    print("Hola, mensaje desde un hilo!")
    time.sleep(50)

thread_1 = threading.Thread(target=tarea)
thread_2 = threading.Thread(target=tarea)
thread_3 = threading.Thread(target=tarea)

print ("Hola, mesaje desde el programa  principal")
thread_1.start()
thread_2.start()
thread_3.start()
time.sleep(50)

