#tri selection 

import time
import random

def listgenerator(n):
    l = []
    for i in range(n):
        a = random.randint(-1000,10000)
        l.append(a)
    return l
        
randomlist = listgenerator(1000)
 
def tri_selection(liste):
    #start = time.time()
    passage = 0
    for i in range(len(liste)):
        mini = i
        for j in range(i+1, len(liste)):
            if liste[mini] > liste[j]:
                mini = j
                
        X = liste[i]
        liste[i] = liste[mini]
        liste[mini] = X
        passage +=1
       
    return print("liste triée : \n {} \n nombre de passage : {}".format(liste,passage))
    #return ("liste rangé :\n{} \n time elapsed : {}".format(liste, time.time() - start))
            
tri_selection(randomlist)
