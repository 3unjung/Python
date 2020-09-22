class Stats(object):
    def __init__(self, hp, force, inteligence, agilite, chance):
        self.hp = hp  # Je veux que la valeur soit = à l'argument
        self.force = force  # Je veux que la valeur soit = à l'argument
        self.inteligence = inteligence  # Je veux que la valeur soit = à l'argument
        self.agilite = agilite  # Je veux que la valeur soit = à l'argument
        self.chance = chance  # Je veux que la valeur soit = à l'argument

    def __str__(self):
        return f"{self.hp} Points de vie, {self.force} Force,{self.inteligence} Inteligence, {self.agilite}, {self.chance} Chance"


class Personnage(object):
    statistiques = Stats(hp=1000, force=100, inteligence=100, agilite=100, chance=100)  # Appel le constructeur de Stats

    def __init__(self):  # Constructeur de Personnage
        # Notre personnage contient les compétences si dessous
        self.name = "Nom par défaut"
        self.skills = ["Flamiche", "Coup de poing", "Coup de pied"]  # Liste de compétences

    def informations(self):
        self.name = input("Saisissez le nom de votre personnage:\n")
        print(
            f"Bienvenue {self.name}, voici vos caractéristiques: {self.statistiques.hp} Points de vie,"
            f" {self.statistiques.force} Force, "f"{self.statistiques.inteligence} Inteligence,"
            f" {self.statistiques.agilite} Agilité, {self.statistiques.chance} Chance\n.")

    def runGame(self):

        while True:
            duTexte = "Sélectionner une compétence pour attaquer:"
            competence = ""
            for i in range(len(self.skills)):
                competence += f"{i + 1} : {self.skills[i]}\n"

            skillsChoice = int(input(f"{duTexte}\n{competence}\n"))

            if skillsChoice <= 0 or skillsChoice > len(self.skills):
                print("Veuillez choisir une compétence valide")
            else:
                print(f"{self.name} lance {self.skills[skillsChoice - 1]}")
            break


if __name__ == '__main__':
    player = Personnage()  # Appel la class Personnage
    player.informations()  # Accède à la méthode de la classe Personnage
    player.runGame()
