import threading

suma = 0

def funcion():
    print("Iniciando hilo")
    global suma
    suma = suma + 5
    print("Variable global modificada")

print("Inicio programa principal")
print("Valor Inicial: " + str(suma))

thread_1=threading.Thread(target=funcion)
thread_2=threading.Thread(target=funcion)
thread_3=threading.Thread(target=funcion)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

print("Valor Final: " + str(suma))




