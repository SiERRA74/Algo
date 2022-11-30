#tri en bulles(simple)

tablo = [10,11, 3, 7, 5, 2]

def tri_bulles(liste):
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
    return liste

print(tri_bulles(tablo))
