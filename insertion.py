#tri insertion 

tablo = [4,3,12,-10,35,-22,44,15,2]

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
            
print(tri_selection(tablo))
