#tri en bulles(simple)

import time
import random
#tri en bulles(simple)
def listgenerator(n):
    l = []
    for i in range(n):
        a = random.randint(-1000,10000)
        l.append(a)
    return l
        
randomlist = listgenerator(1000)


def tri_bulles(liste):
    start = time.time()    
    echange = True
    passage = 0
    while echange == True:
        echange = False
        passage = 0
        for i in range(0 , len(liste)-1 - passage):
            if liste[i] > liste[i+1]:
                echange = True
                liste[i], liste[i+1] = liste[i+1],liste[i]
            passage += 1
    return ("liste rangé :\n{} \n ".format(liste, time.time() - start))

print(tri_bulles(randomlist),"\n", time.time())
