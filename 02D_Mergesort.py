import threading
import time
import random

number = [0, 0]
choosing = [False, False]

def proceso(id, other):
    for _ in range(3):  # cada proceso entra 3 veces a la sección crítica
        
        # Paso 1: Sort (elegir número)
        choosing[id] = True
        number[id] = 1 + number[other]   # para 2 procesos basta mirar al otro
        choosing[id] = False

        # Paso 2: Merge (esperar turno si el otro tiene prioridad)
        while choosing[other]:
            pass  # espero a que termine de elegir

        while number[other] != 0 and (number[other], other) < (number[id], id):
            pass  # espero si el otro tiene prioridad

        # --- Sección crítica ---
        print(f"Proceso {id} entra a la sección crítica")
        time.sleep(random.uniform(0.5, 1.5))  # simula trabajo
        print(f"Proceso {id} sale de la sección crítica")

        number[id] = 0

# Crear dos hilos
t0 = threading.Thread(target=proceso, args=(0, 1))
t1 = threading.Thread(target=proceso, args=(1, 0))

t0.start()
t1.start()

t0.join()
t1.join()