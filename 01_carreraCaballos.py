from threading import Thread, Lock
from time import sleep

gano = False
lock = Lock()

def caballo(num):
    global gano
    for i in range(1, 4):
        print(f"Corre {num}")
        sleep(2)
        with lock:
            if gano:
                return
        
    with lock:
        if not gano:
            gano = True
            print(f"El caballo {num} llegó a la meta")

threads = []

for i in range(1, 11):
    thread = Thread(target=caballo, args=(i,))
    threads.append(thread)
    
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


