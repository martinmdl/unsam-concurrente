# Para ejemplificar la solución por turnos para exclusión mutua voy a hacer una
# analogía donde una familia de 3 integrantes tiene que usar el baño (critical section) a la mañana.
# Padre: turno 1, Madre: turno 2, Hijo: turno 3

import threading
import time
turno = 1
tInicial = time.time()


def rutinaBañoPadre():

    global turno
    global tInicial

    print(f"El padre está desayunando ({(time.time() - tInicial):.4f})") # non-critical section
    time.sleep(1) # Simula el tiempo que tarda en desayunar

    while turno != 1:
        time.sleep(0.001) # Await(turn = 1) improvisado (no esta en el módulo threading)

    print(f"El padre está usando el baño ({(time.time() - tInicial):.4f})") # critical section
    time.sleep(1.5) # Simula el tiempo que tarda en bañarse

    turno = 2

def rutinaBañoMadre():

    global turno
    global tInicial

    print(f"La madre está desayunando ({(time.time() - tInicial):.4f})")
    time.sleep(1)

    while turno != 2:
        time.sleep(0.001)

    print(f"La madre está usando el baño ({(time.time() - tInicial):.4f})")
    time.sleep(1.5)

    turno = 3

def rutinaBañoHijo():

    global turno
    global tInicial

    print(f"El hijo está desayunando ({(time.time() - tInicial):.4f})")
    time.sleep(1)

    while turno != 3:
        time.sleep(0.001)

    print(f"El hijo está usando el baño ({(time.time() - tInicial):.4f})")
    time.sleep(1.5)

    turno = 1

threads = [
    threading.Thread(target=rutinaBañoPadre),
    threading.Thread(target=rutinaBañoMadre),
    threading.Thread(target=rutinaBañoHijo)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Todos terminaron de usar el baño ({(time.time() - tInicial):.4f})")