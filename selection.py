#tri selection 

import random

def listgenerator(n):
    l = []
    for i in range(n):
        a = random.randint(-1000,10000)
        l.append(a)
    return l
        
randomlist = listgenerator(1000)
 
def tri_selection(liste):
   for i in range(len(liste)):
       mini = i
       for j in range(i+1, len(liste)):
           if liste[mini] > liste[j]:
               mini = j
                
       X = liste[i]
       liste[i] = liste[mini]
       liste[mini] = X
   return liste
            
print(tri_selection(randomlist))
