# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:49:56 2020

@author: Eunjung
"""

"""
    * le constructeur est une fonction spéciale
    * il permet d'obliger le requis des informations
    * nécessaire pour la classe """
# self = this
# methode = fonction
# timedelta = différence de temps sous forme jj/ss/micros
# gère les décimales automatiquement
    
from datetime import datetime
class Employe:
    def __init__(self, nom, prenom, dateEmbauche, fonction, salaire, service):
        self.nom = nom # assosie une valeur de la classe Employe à nom avec .
        self.prenom = prenom
        self.dateEmbauche = dateEmbauche
        self.fonction = fonction
        self.salaire = salaire
        self.service = service
        
    def ancient(self): # définie une méthode pour connaitre l'ancienneté de l'employé
        timedelta = datetime.now() - self.dateEmbauche # calcule la différence de temps entre maintenant et la date d'embauche
        return timedelta.days / 365 #  calcule le nombre d'année depuis la date d'embauche
    
if __name__ == "__main__":
    el = Employe("Margaux", "Acloque", datetime(2019,8,15),"Etudiante", "17", "développeuse")
    print("Depuis ", el.ancient(), "année(s) !") 
   
   
