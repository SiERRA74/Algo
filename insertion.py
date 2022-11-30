#tri par insertion
tablo = [4,3,-12,12,10,15,2]

def tri_insertion(liste): 
    for i in range(1, len(liste)): 
        Y = liste[i] 
        X = i-1
        while X >= 0 and Y < liste[X] : 
                liste[X + 1] = liste[X] 
                X -= 1
        liste[X + 1] = Y
    return liste

print(tri_insertion(tablo))
