# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 16:11:50 2025

@author: qtoul
"""

from random import randint

liste_classe=["Voleur", "Mage", "Guerrier", "Fermier"]
level=1
pv_base=10
force_base=10
classe=None
nom=str
pv=None
force=None
sort=["Boule de feu", "Esquive", "Gel"]



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
    
    print(f"Votre personnage est : {nom} \n C'est un {classe} \n Il a {pv} points de vie \n Sa force est de {force}")
    print("\n")
    combat_squelette()

def combat_squelette():
    """fonction pour le combat avec le squelette"""
    global pv, level, force
    pv_squelette=10
    while pv_squelette>0 and pv>0:
        print(f"Le Squelette a {pv_squelette}")
        rep=str(input("Voulez vous attaquer ? (y/n) : "))
        if rep =="y":
            pv_squelette-= randint(2, 5)*force
            print(f"Le Squelette a {pv_squelette}")
            pv-=1
            print(f"Le Squelette vous fait 1 dégât, il vous reste {pv}")
        else:
            print("Vous fuyez")
            break
    if pv_squelette<=0:
        print("Vous avez gagné et obtenu 1 niveau")
        level +=1
        pv+=20
        print(f"Vous gagnez 20pv, vous avez donc {pv} pv")
    else:
        print("Le squelette a gagné")
    force*=1.2
    pv*=1.5
    print(f"Votre force augmente de 20%, et votre vie de 50%. Vous avez donc : {force} force et {pv} pv")
    print("\n")
    combat_golem()

def sort(choix, pv_ennemie):
    """choix du sort"""
    global force
    if choix==1:
        if randint(1, 100)<=10:
            print("Echec du sort")
        else:
            pv_ennemie-= force + 10
    elif choix==2:
        if randint(1, 100)<=20:
            print("Echec du sort")
        else:
            pv_ennemie-= force + 20
    else:
        if randint(1, 100)<=50:
            print("Echec du sort")
        else:
            pv_ennemie-= force*10
    return pv_ennemie
        
    
def combat_golem():
    """combat du golem"""
    global pv, level, force, sort
    print("Vous avez 3 nouveaux sorts : boule de feu (force + 10 dégâts (10% de taux d'echec)), eclair (force+20 (20% d'echec)')), Gel (force * 10 (50% d'echec)'))")
    pv_golem=1000
    print(f"Un golem avec {pv_golem} pv apparait")
    while pv_golem>0 and pv>0:
        choix=int(input("Choisissez un sort (1, 2 ou 3) : "))
        pv_golem= sort(choix, pv_golem)
        print(f"Le golem a encore {pv_golem}")
        degat_golem=5
        pv-=5
        print(f"Le golem vous fait 5 dégâts. Il vous reste {pv}")
    if pv_golem<=0:
        print("Vous avez gagné")
        print("vous passez niveau 5")
        force*=2.5
        pv+=150
        print(f"Votre force augmente de 250%, et votre vie de 150pv. Vous avez donc : {force} force et {pv} pv")
    else:
        print("Le golem vous a écrasé")
    print("\n")
    
    
if __name__ == "__main__":
    perso_rpg()   