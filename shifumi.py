"""
    * Begin 05/08/19
    * Update 05/08/19
"""
import random
import sys

print("Bienvenue, l'ordinateur choisis aléatoirement pierre, feuille ou ciseau.\n"
      "Vous avez le choix entre : \n"
      "1 pour la pierre\n"
      "2 pour la feuille\n"
      "3 pour le ciseau\n"
      "0 pour quitter la partie.")


def shifumi():
    choix = random.randint(1, 3)
    answer = int(input("Choisissez votre réponse :"))
    print()
    print(f"Vous avez le choix entre :\n"
          "1 pour la pierre\n"
          "2 pour la feuille\n"
          "3 pour le ciseau\n"
          "0 pour quitter la partie.")

    if answer == 0 or answer > 3:
        print(f"À la prochaine !")
        sys.exit(0)

    if choix == answer:
        print(f"Égalité")
    elif choix == 1 and answer == 3:
        print(f"La pierre gagne contre le ciseau, perdu ...")
    elif choix == 2 and answer == 1:
        print(f"La feuille gagne contre la pierre, perdu !")
    elif choix == 2 and answer == 3:
        print(f"La feuille perd contre le ciseau, gagné !")
    elif choix == 3 and answer == 1:
        print(f"Le ciseau perd contre la pierre, Gagné !")
    elif choix == 3 and answer == 2:
        print(f"Le ciseau gagne contre la feuille, perdu")


while True:
    shifumi()
