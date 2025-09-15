import random
import threading

def sort1(list):
    list.sort() # async
    s1.release()

def sort2(list):
    list.sort() # async
    s2.release()

def merge(listA, listB):
    s1.acquire()
    s2.acquire()
    newList = listA + listB # critical section
    newList.sort()
    print(newList)
    return newList

listaDesordenada = [random.randint(0, 1000) for _ in range(100)] # 100 enteros entre 0 y 1000

s1 = threading.Semaphore(0)
s2 = threading.Semaphore(0)

centro = len(listaDesordenada) // 2

half1 = listaDesordenada[:centro]
half2 = listaDesordenada[centro:]

threads = [
    threading.Thread(target=sort1, args=(half1,)),
    threading.Thread(target=sort2, args=(half2,)),
    threading.Thread(target=merge, args=(half1, half2))
]

for t in threads: t.start()
for t in threads: t.join()