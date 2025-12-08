# ** Coding:UTF-8 **
import random
# nomperso = str(input("Donne moi le nom de ton perso"))
# classe = str(input("Donne moi la classe de ton perso"))
niveau= 1 
pv= int(input("donne ses pvs "))
force= 100
pvsquelette=10
golem=50
#print("Ton personnage", nomperso ,"est un", classe, "de niveau", niveau , "avec les pv ", pv , "et la force de ", force ,   ) k


degat = random.randint(5,15)

if degat>=pvsquelette:

    print("le squelette est Vaincu")
    niveau+=1
    print(niveau)
else:
    print("le squelette se moque de toi")




while golem>0 and pv >0:
    print("il te reste ",pv , "pv et le golem à ",golem, "pv")
    tableau = {
    "1": ("Coup d'épée", random.randint(10, 14)),
    "2": ("Lancer de dague", random.randint(2, 22)),
    "3": ("Boule de feu", random.choice([0, 1]))
}
    print(tableau)
    choixattaque=(str(input("choisi l'attaque que tu veux ")))
    golem-=tableau[choixattaque][1]
    pv-=7
    
if golem<pv:
    print("Golem Vaincu")
    print("il te reste ",pv)
else:
    print("le Golem t'a shit on")