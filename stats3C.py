import time
import random


def listgenerator(n):
    l = []
    for i in range(n):
        a = random.randint(-1000,10000)
        l.append(a)
    return l

def tri_bulle(liste):
    #start = time.time()    
    echange = True
    comparaison = 0
    echanges = 0
    while echange == True:
        echange = False
        nion = 0
        for i in range(0 , len(liste)-1 - nion):
            if liste[i] > liste[i+1]:
                echange = True
                liste[i], liste[i+1] = liste[i+1],liste[i]
                echanges +=3
            comparaison += 1
    return comparaison + echanges
  
  
def tri_selection(liste):
    comparaison = 0
    echange = 0
    for i in range(len(liste)):
        mini = i
        for j in range(i+1, len(liste)):
            if liste[mini] > liste[j]:
                comparaison +=1
                mini = j
                
        X = liste[i]
        liste[i] = liste[mini]
        liste[mini] = X
        echange +=3
    return comparaison + echange
  
  
def tri_insertion(liste): 
    comparaison = 0
    echanges = 0
    #start = time.time()
    for i in range(1, len(liste)): 
        Y = liste[i] 
        X = i-1
        while X >= 0 and Y < liste[X] : 
                liste[X + 1] = liste[X] 
                echanges +=3
                X -= 1
        liste[X + 1] = Y
        comparaison += 1
    return comparaison+echanges
  
def tri_bulle_opti(liste):
    comparaison = 0
    echanges = 0
    #start = time.time()
    for i in range(len(liste)-1):
        for j in range(0, i-1):
            if liste[j] > liste[j+1]:
                liste[j+1], liste[j] = liste[j], liste[j+1]
                sorted = False
                echanges +=3
            comparaison +=1
    sorted = True
    if sorted == True:
        return comparaison+echanges
     

def stats(mini, maxi, pas, preci,def_tri):
    for i in range(mini, maxi + pas, pas):
        start = time.time()
        cout = 0
        for n in range(preci):
            liste = [random.randint(0, 100) for _ in range(i)]
            cout += def_tri(liste)
        total = round((cout / preci * 0.1),2) 
        print("len de liste : {}\ncoût moyen {} \ncout en temps :{}\n".format(i, total , time.time()-start)
stat(150, 200, 10, 500,tri_selection)

  
      
stats_tri_selec = stats(10,20,5,10,tri_selection())
stats_tri_inser = stats(10,20,5,10,tri_insertion())
stats_tri_bulle = stats(10,20,5,10,tri_bulle())
stats_tri_bulle_opti = stats(10,20,5,10,tri_bulle_opti())
      
print(stats_tri_selec, "\n",stats_tri_inser, "\n",stats_tri_bulle, "\n",stats_tri_bulle_opti, "\n")
