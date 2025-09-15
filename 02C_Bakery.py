import threading
import time

tInicial = time.time()

N = 3 # Cantidad de procesos
choosing = [False] * N    # indica si un proceso está eligiendo número
number = [0] * N          # np, nq, nr

def bakery(id: int):

    for _ in range(2):  # cada proceso intenta ejecutar SC 2 veces

        # ----- Elegir número -----
        choosing[id] = True
        number[id] = 1 + max(number)   # elijo un número mayor al de todos
        choosing[id] = False

        # ----- Esperar turno -----
        for j in range(N):
            if j == id:
                continue
            while choosing[j]:
                pass  # espero a que termine de elegir
            while number[j] != 0 and (number[j], j) < (number[id], id):
                pass  # espero si otro tiene prioridad

        # ----- Sección crítica -----
        print(f"{(time.time() - tInicial):.2f}: Proceso {id} ENTRA a la SC")
        time.sleep(1)
        print(f"{(time.time() - tInicial):.2f}: Proceso {id} SALE de la SC")
    
        number[id] = 0


threads = [threading.Thread(target=bakery, args=(i,)) for i in range(N)]

for t in threads:
    t.start()

for t in threads:
    t.join()