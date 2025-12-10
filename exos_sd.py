# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 16:11:50 2025

@author: qtoul
"""

from random import randint
import random as rd

liste_classe=["Voleur", "Mage", "Guerrier", "Fermier"]
liste_sort=["Coup d'épée (1)", "Lancer de dague (2)", "Boule de feu (3)"]

level=1
pv_base=10
force_base=10
classe=None
nom=str
pv=None
force=None
sort=None
Golem_vivant=True


def perso_rpg():
    """definis un personnage pour le jeu rpg"""
    
    global pv, force, level
    nom= str(input("Choisissez votre nom : "))
    print(liste_classe)
    selec_classe=(int(input("Choisissez votre classe (selectionnez l'indice de la classe (1-4) : ")))-1
    
    if selec_classe==0:
        classe="Voleur"
        pv=pv_base*1.2
        force=force_base*0.9
    elif selec_classe==1:
        classe="Mage"
        pv=pv_base*1
        force=force_base*1.5
    elif selec_classe==2:
        classe="Guerrier"
        pv=pv_base*3
        force=force_base*2
    else:
        classe="Fermier"
        pv=pv_base*4
        force=force_base*0.5
    
    print(f"Votre personnage est : {nom} \n C'est un {classe} \n Il a {pv} points de vie \n Sa force est de {force}. \n")
    choix_combat()

def choix_combat():
    rep=str(input("Voulez vous attaquer ? (y/n) : "))
    if rep =="y":
        sort_golem()
    else:
        print("Vous fuyez... (Sale merde)")
        

def sort_golem():

    global pv, level, force, Golem_vivant
    pv_squelette=50
    print(liste_sort)
    while Golem_vivant==True:
        selec_sort=(int(input("Choisissez votre sort (1-3) : ")))-1
        if selec_sort==0:
            sort="Coup d'épée"
            Cde=randint(10, 14)
            pv_squelette-=Cde
            Degat=Cde
        elif selec_sort==1:
            sort="Lancer de dague"
            Ldg=randint(2, 22)
            pv_squelette-=Ldg
            Degat=Ldg
        elif selec_sort==2:
            sort="Boule de feu"
            Bdf=rd.choice([0, 20])
            pv_squelette-=Bdf
            Degat=Bdf
        else:
            print("OUPS ! Veuillez choisir un nombre entre 1 et 3 pour séléctionner votre sort !")
        
        pv-=7
        print(f"Les sort utilisé est {sort}. \n Vous avez fait {Degat} dégâts. \n Le Golem a maintenant {pv_squelette} PV. \n Le golem vous inflige 7 dégâts. \n Vous avez maintenant {pv} PV. \n")


        if pv_squelette<=0:
            Golem_vivant=False
            if pv>1:
                print("BRAVO ! Vous avez sauver le village !")
                coffre()
            else:
                print("Le golem est mort, mais vous aussi...")
        else:
            Golem_vivant=True
    

def coffre():

    Choix=True
    i=0
    Score_Arme=int(rd.randint(1, 20))
    
    while Choix==True:
        selec_nombre=(int(input("Choisissez un nombre entre 1 et 20 : ")))
        
        if i<4:
            if selec_nombre>Score_Arme:
                print("Trop Haut \n")
                Choix=True
                i=i+1
            elif selec_nombre<Score_Arme:
                print("Trop bas \n")
                Choix=True
                i=i+1
            elif selec_nombre==Score_Arme:
                print("BRAVO ! Tu as gagné l'ARME ULTIME \n")
                Choix=False
                inventaire()
            else:
                print("J'ai dis entre 1 et 20 mec... \n")

        else:
            print("Vous perdez vos pièces d'or ! \n")
            Choix=False
    
def inventaire():
    print("Voici ton inventaire : \n - Arme Ultime \n - 20 Pièces d'or \n")
           
    

if __name__ == "__main__":
    perso_rpg()   