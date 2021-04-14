import os
import multiprocessing
import time


def tarea():
    nombre = multiprocessing.current_process().name
    procId = multiprocessing.current_process().pid
    pprocId = os.getppid()
    print(f"Este es el proceso {nombre} con PID = {str(procId)} y PPID = {pprocId}")
    time.sleep(10)

if __name__ == '__main__':


    worker_1 = multiprocessing.Process( name='tarea 1',target=tarea,)
    worker_2 = multiprocessing.Process( name='tarea 2',target=tarea,)

    worker_1.start()
    worker_2.start()
    print(f"Este es el proceso principal con PID = {str(os.getppid())}")
    worker_1.join()
    worker_2.join()
