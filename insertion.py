#tri insertion 

tablo = [4,3,12,10,35,22,44,15,2]

def tri_selection(tab):
   for i in range(len(tab)):
       mini = i
       for j in range(i+1, len(tab)):
           if tab[mini] > tab[j]:
               mini = j
                
       X = tab[i]
       tab[i] = tab[mini]
       tab[mini] = X
   return tab
            
print(tri_selection(tab))
