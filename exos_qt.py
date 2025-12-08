from random import randint

liste_classe=["Voleur", "Mage", "Guerrier", "Fermier"]
level=1
pv_base=10
force_base=10
classe=None
nom=str
pv=None
force=None


def perso_rpg():
    """definis un personnage pour le jeu rpg"""
    
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
        else:
            print("Vous fuyez")
            break
    if pv_squelette<=0:
        print("Vous avez gagné et obtenu 1 niveau")
        level +=1
    else:
        print("Le squelette a gagné")

if __name__ == "__main__":
    perso_rpg()   