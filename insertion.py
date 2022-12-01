#tri par insertion
import time
import random

def listgenerator(n):
    l = []
    for i in range(n):
        a = random.randint(-1000,10000)
        l.append(a)
    return l
        
randomlist = listgenerator(1000)

def tri_insertion(liste): 
    passage = 0
    start = time.time()
    for i in range(1, len(liste)): 
        Y = liste[i] 
        X = i-1
        while X >= 0 and Y < liste[X] : 
                liste[X + 1] = liste[X] 
                passage +=1
                X -= 1
        liste[X + 1] = Y
    print("liste rangé :\n {} \n nombre de passage: {}".format(liste, passage))
    #print("liste rangé :\n{} \n time elapsed : {}".format(liste, time.time() - start))
    

tri_insertion(randomlist)
