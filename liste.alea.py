from random import randint 

def liste_alea(n):
    L = []
    for k in range(n):
        L.append(randint(0,100))
    return L
    
def pos_min(L):
    pos = 0
    for i in range(1, len(L)):
        if L[i] < L[pos]:
            pos = i
    return pos 

def tri_min(L):
    for i in range (0,len(L)-2) :
        Lfin = L[i:]
        pos = pos_min(Lfin)
        temp = L [i]
        L[i] = L[i+pos]
        L[i+pos] = temp
    return L
        
            