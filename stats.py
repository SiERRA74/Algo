
import time
import random

def listgenerator(n):
    l = []
    for i in range(n):
        a = random.randint(-1000,10000)
        l.append(a)
    return l


randomlist = listgenerator(1000)


def tri_bulles(liste):
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
                echanges +=1
            comparaison += 1
            
    print("liste triée : \n {} \n nombre de comparaisons : {}\n comtpeurs d'échange : {} \n".format(liste,comparaison,echanges*3))
    #print("liste trié :\n{} \n temps écoulé : {} ".format(liste, time.time() - start))
    return [comparaison,echanges*3]

def tri_selection(liste):
    #start = time.time()
    comparaison = 0
    echanges = 0
    for i in range(len(liste)):
        mini = i
        for j in range(i+1, len(liste)):
            echanges += 1
            if liste[mini] > liste[j]:
                mini = j
                
        X = liste[i]
        liste[i] = liste[mini]
        liste[mini] = X
        comparaison +=1
       
    print("liste triée : \n {} \n nombre de comparaison : {}\n nombre d'échanges : {}".format(liste,comparaison,echanges))
    #print("liste rangé :\n{} \n time elapsed : {}".format(liste, time.time() - start))
    return [comparaison,echanges*3]

def tri_insertion(liste): 
    comparaison = 0
    echanges = 0
    start = time.time()
    for i in range(1, len(liste)): 
        Y = liste[i] 
        X = i-1
        while X >= 0 and Y < liste[X] : 
                liste[X + 1] = liste[X] 
                echanges +=1
                X -= 1
        liste[X + 1] = Y
        comparaison += 1
    print("liste rangé :\n {} \n nombre de passage: {}".format(liste, comparaison))
    #print("liste rangé :\n{} \n time elapsed : {}".format(liste, time.time() - start))
    return [comparaison,echanges*3]
  
  
def tri_bulle_opti(liste):
    comparaison = 0
    echanges = 0
    #start = time.time()
    for i in range(len(liste)-1):
        for j in range(0, i-1):
            if liste[j] > liste[j+1]:
                liste[j+1], liste[j] = liste[j], liste[j+1]
                sorted = False
                echanges +=1
    sorted = True
    if sorted == True:
        print("liste rangé :\n {} \n nombre de comparaison: {}\n nombre d'échanges: {}".format(liste, comparaison, echanges))
        #print("liste rangé :\n{} \n time elapsed : {}".format(liste, time.time() - start))
        return [comparaison,echanges]
      
      
stats_bulle_opti = tri_bulle_opti(randomlist)  
stats_bulles = tri_bulles(randomlist)
stats_selection = tri_selection(randomlist)
stats_insertion = tri_insertion(randomlist)
print("_______________________// nb comparaisons // nb echanges.        (1 échanges = 3 affectations)") 
print("tri par selection      // ", stats_selection[0],"    ", stats_selection[1]  )
print("tri par insertion      // ", stats_insertion[0],"    ",stats_insertion[1])
print("tri à bulles           // ", stats_bulles[0],"    ",stats_bulles[1])
print("tri à bulles optimisé  // ", stats_bulle_opti[0],"    ",stats_bulle_opti[1]  )
