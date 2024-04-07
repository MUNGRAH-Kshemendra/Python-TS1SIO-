import pygame

def ouvrir_fenetre():
    taille_case = 20
    taille_fenetre_H = taille_case * 40
    taille_fenetre_V = taille_case * 24
    pygame.init()
    fenetre = pygame.display.set_mode((taille_fenetre_H, taille_fenetre_V))
    return fenetre

def afficher_grille(fenetre, Tab):
    taille_case = 20
    for i in range(len(Tab)):
        for j in range(len(Tab[i])):
            if Tab[i][j] == 1:
                pygame.draw.rect(fenetre, (0, 0, 0), (j*taille_case, i*taille_case, taille_case, taille_case))
            else:
                pygame.draw.rect(fenetre, (255, 255, 255), (j*taille_case, i*taille_case, taille_case, taille_case))
    pygame.display.flip()

def fermer_fenetre():
    pygame.quit()

if __name__ == "__main__":
    from random import randint
    from time import sleep
    fenetre = ouvrir_fenetre()
    Tab = [[randint(0, 1) for C in range(40)] for L in range(24)]    
    afficher_grille(fenetre, Tab)
    sleep(2)
    fermer_fenetre()