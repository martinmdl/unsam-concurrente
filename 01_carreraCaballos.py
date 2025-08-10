from threading import Thread, Lock
from time import sleep

gano = False
lock = Lock()

def caballo(num, vueltas):
    global gano
    for i in range(1, vueltas + 1):
        print(f"Caballo {num} - vuelta {i}")
        sleep(2)
        with lock:
            if gano:
                return
        
    with lock:
        if not gano:
            gano = True
            print(f"El caballo {num} llegó a la meta")

def main():
    threads = []

    cantCaballos = int(input("Ingrese la cantidad de caballos: "))
    cantVueltas = int(input("Ingrese la cantidad de vueltas: "))

    for i in range(1, cantCaballos + 1):
        thread = Thread(target=caballo, args=(i, cantVueltas))
        threads.append(thread)
        
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()


