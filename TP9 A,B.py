from random import randint 
def choix_ordi():
    L = []
    for k in range(3):
        L.append(randint(1,5))
        return L 

print (choix_ordi())

def saisie():
    continuer = True
    while continuer == True:
        n = int(input("Saisir un nombre entier entre 1 et 5 :"))
        if n >= 1 and n <= 5:
            continuer = False
    return n

print (saisie())

def essai():
    L = []
    for k in range(3):
        L.append(saisie())
    return L


bonne_rep = choix_ordi()
n = 0
victoire = False 
while victoire == False:
    n = n + 1
    print ("tentative numéro" , n)
    tentative = essai()
    if tentative == bonne_rep:
        victoire = True
print ("Code trouvé en ", n,"tentive)
       