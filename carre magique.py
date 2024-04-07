Tab = [[8,3,4],[4,5,6],[7,8,9]]
def est_carre(Tab):
    nb_ligne = len(Tab)
    nb_colone = len(Tab[0])
    if nb_ligne == nb_colone:
        return True
    else:
        return False

def somme(L):
    s = 0
    for k in range(len(L)):
        s = s + L[k]
    return s

def ligne(Tab,n):
    return Tab[n]

def colonne(Tab,n):
    L = []
    for k in range(len(Tab)):
        L.append(Tab[k][n])
    return L

def diagonales(Tab):
    diag1 = []
    diag2 = []
    if est_carre(Tab):
        for k in range(len(Tab)):
            diag1.append(Tab[k],[k])
            diag2.append(Tab[k][len(Tab)-1-k])
    return diag1,diag2
   
print(diagonales(Tab))

def est_magique(Tab):
    if est_carre == True:
        diag1,diag2 = diagonales(Tab)
        liste = [somme(diag1),somme(diag2)]
        for n in range(len(Tab)):
            liste.append(somme(ligne(Tab,n)))
            liste.append(somme,(colonne(Tab,n)))
            for k in range (1,len(liste)):
        if liste [0] != liste[k]:
            test = False
        return test
    else:
        return False
print(est_carre)