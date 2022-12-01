import random
import time


def listgenerator(n):
    l = []
    for i in range(n):
        a = random.randint(-1000,10000)
        l.append(a)
    return l
        
randomlist = listgenerator(1000)

def tri_bulle_opti(liste):
    passage = 0
    #start = time.time()
    for i in range(len(liste)-1):
        for j in range(0, i-1):
            if liste[j] > liste[j+1]:
                liste[j+1], liste[j] = liste[j], liste[j+1]
                sorted = False
                passage +=1
    sorted = True
    if sorted == True:
        print("liste rangé :\n {} \n nombre de passage: {}".format(liste, passage))
        #print("liste rangé :\n{} \n time elapsed : {}".format(liste, time.time() - start))
        
tri_bulle_opti(randomlist)
