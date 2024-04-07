def liste_diviseurs(n):
    L = []
    racine = int(n ** 0.5)
    for d in range (1,racine+1):
       if n % d == 0: #si n est divible par d 
           L.append(d)
           if d != n//d: #cette ligne représente les grands diviseurs ici on évite d'avoir des doubles dans la liste    
               L.append(n//d)#pour avoir les plus grand diviseurs
    return L

#print (liste_diviseurs(100))


def liste_premiers(n):
    L = []
    for k in range (1,n+1):
        if len(liste_diviseurs(k)) == 2:#il n'a que deux diviseurs c'est un nombre premier
            L.append(k)
    return L

#print(liste_premiers(20))
def decomposition(n):
    L = []
    P = liste_premiers(n)
    i = 0
    while n > 1 and i < len(P):
        if n % P[i] == 0:#trouver le premier diviseur
            L.append(P[i])
            n = n // P[i]
        else :
            i = i + 1#parcour la liste
    return L

print (decomposition(28))#test du nombre 28 pour avoir sont produit de nombre premier

def pgcd_naif(a,b):
    pgcd = 1
    m = min(a,b)
    P = liste_premiers(m)
    i = 0
    while a > 1 and b > 1 and i < len(P):
        if a % P[i] == 0 and b % P[i] == 0:
            pgcd = pgcd * P[i]
            a = a // P[i]
            b = b // P[i]
        else:
            i = i + 1
    return pgcd

#print(pgcd_naif(23, 12))
#print(pgcd_naif(2345, 1234))
#print(pgcd_naif(234567, 123456))

def pgcd_Euc_iteratif(a,b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a
#print(pgcd_Euc_iteratif(23, 12))
#print(pgcd_Euc_iteratif(2345, 1234))
#print(pgcd_Euc_iteratif(234567, 123456))
def pgcd_Euc_recursif(a,b):
    if a % b == 0:
        return b
    else:
        r = a % b
    return pgcd_Euc_recursif(b,r)
print(pgcd_Euc_recursif(23, 12))
print(pgcd_Euc_recursif(2345, 1234))
print(pgcd_Euc_recursif(234567, 123456))
        