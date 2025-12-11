# -*- coding: utf-8 -*-
"""
Optimisation du RPG
"""

from random import randint, choice

# Données du jeu
CLASSES = {
    1: ("Voleur",   1.2, 0.9),
    2: ("Mage",     1.0, 1.5),
    3: ("Guerrier", 3.0, 2.0),
    4: ("Fermier",  4.0, 0.5)
}

SORTS = {
    1: ("Coup d'épée",      lambda: randint(10, 14)),
    2: ("Lancer de dague",  lambda: randint(2, 22)),
    3: ("Boule de feu",     lambda: choice([0, 20]))
}


def perso_rpg():
    """Création du personnage"""
    pv_base = 10
    force_base = 10

    nom = input("Choisissez votre nom : ")

    for i, (c, _, _) in CLASSES.items():
        print(f"{i} - {c}")

    # Sélection classe sécurisée
    while True:
        try:
            choix = int(input("Choisissez votre classe (1-4) : "))
            if choix in CLASSES:
                break
        except ValueError:
            pass
        print("Veuillez entrer un nombre entre 1 et 4.")

    classe, pv_mult, force_mult = CLASSES[choix]

    pv = pv_base * pv_mult
    force = force_base * force_mult

    print(f"\nVotre personnage est : {nom}")
    print(f"Classe : {classe}")
    print(f"PV : {pv}")
    print(f"Force : {force}\n")

    choix_combat(pv, force)


def choix_combat(pv, force):
    rep = input("Voulez-vous attaquer ? (y/n) : ").lower()
    if rep == "y":
        combat_golem(pv, force)
    else:
        print("Vous fuyez... (Sale merde)")


def combat_golem(pv, force):
    pv_golem = 50

    print("\n--- LISTE DES SORTS ---")
    for i, (nom_sort, _) in SORTS.items():
        print(f"{i} - {nom_sort}")

    while pv_golem > 0 and pv > 0:

        # Choix sort sécurisé
        while True:
            try:
                choix = int(input("\nChoisissez votre sort (1-3) : "))
                if choix in SORTS:
                    break
            except ValueError:
                pass
            print("Choix invalide.")

        nom_sort, degats_fct = SORTS[choix]
        degats = degats_fct()
        pv_golem -= degats
        pv -= 7

        print(f"\nVous utilisez : {nom_sort}")
        print(f"Dégâts infligés : {degats}")
        print(f"PV restants du golem : {pv_golem}")
        print(f"Il vous inflige 7 dégâts. Vos PV : {pv}")

    if pv_golem <= 0:
        print("\nBRAVO ! Vous avez sauvé le village !")
        coffre()
    else:
        print("\nLe golem est mort, mais vous aussi...")


def coffre():
    score = randint(1, 20)
    tentatives = 4

    print("\nVous trouvez un coffre !")

    while tentatives > 0:
        try:
            choix = int(input("Choisissez un nombre entre 1 et 20 : "))
        except ValueError:
            print("Ce n'est pas un nombre !")
            continue

        if choix < 1 or choix > 20:
            print("Entre 1 et 20 j'ai dit...")
            continue

        tentatives -= 1

        if choix > score:
            print("Trop haut !\n")
        elif choix < score:
            print("Trop bas !\n")
        else:
            print("\nBRAVO ! Tu as gagné l'ARME ULTIME !")
            return inventaire()

    print("Vous perdez vos pièces d'or...")


def inventaire():
    print("\nVoici ton inventaire :")
    print(" - Arme Ultime")
    print(" - 20 pièces d'or\n")


if __name__ == "__main__":
    perso_rpg()
