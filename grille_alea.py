from random import randint
from annexe_TP10 import ouvrir_fenetre, afficher_grille, fermer_fenetre
from time import sleep

def grille_alea():
    tab = []
    for L in range(24):
        ligne = []
        for C in range(40):
            ligne.append(randint(0,1))
        tab.append(ligne)
        return tab
    
def nb_voisines_vivantes(T,i,j):
    cpt = 0
    for L in range (i-1,i+2):
        for C in range(j-1,j+2):
            if 0 <= L < 24 and 0 <= C < 40:
                cpt = cpt + T[L][C]
    cpt = cpt - T[i][j]
    return cpt


def generation_suivante(Tab):
    Tab2 = []
    for L in range(24):
        ligne = []
        for C in range(40):
            if Tab [L][C] == 1: #si la cellule est actuelement vivante ou morte
                  if 2 <= nb_voisines_vivantes <= 3:
                      ligne.append(1)
                  else: ligne.append(0)
                  
            else: 
                if nb_voisines_vivantes == 3:
                    ligne.append(1)
                else:
                    ligne.append(0)
                    
                
                  
                  
                  
        Tab2.append(ligne)
    return Tab2

Tab = grille_alea()
fenetre = ouvrir_fenetre()
for etape in range(100):
    afficher_grille(fenetre, Tab)
    sleep(0.1)
    Tab = generation_suivante(Tab)
fermer_fenetre()


