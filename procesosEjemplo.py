import os
import time

def hijo():
    print("Este es el proceso \"hijo\" con PID= %d"%os.getpid())

def padre():
    print("Este es el proceso \"padre\" con PID= %d"%os.getpid())

newRef=os.fork()

if newRef==0:
    hijo()
    time.sleep(10)
else:
    print("Este es el proceso \"padre\" con PID = %d"%os.getpid() + " y mi proceso hijo tiene PID=%d"%newRef)
    padre()
    time.sleep(10)



