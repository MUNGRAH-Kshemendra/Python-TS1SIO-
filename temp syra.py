

def impair(n):
    n = n % 2
    b = bool(n)
    return b

def suivant(n):
    if impair(n) == True:
        return 3*n + 1
    else:
        return n // 2
def nbtermes(n):
        c = 0
        while n!=4:
            n = suivant(n)
            c = c + 1  
        return c

def syra(n) :
    L = []

    while n != 4:
          n = suivant(n)
          L.append(n)
    return L
        
        
        
    






