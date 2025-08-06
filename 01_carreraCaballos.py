from threading import Thread
from time import sleep

gano = False

def caballo(num):
    global gano
    for i in range(1, 4):
        if gano:
            return
        print(f"Corre {num}")
        sleep(2)
    gano = True
    print(f"El caballo {num} ganó la carrera")

threads = []

for i in range(1, 5):
    thread = Thread(target=caballo(i))
    threads.append(thread)
    
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


