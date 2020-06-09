# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 18:14:49 2020

@author: Eunjung
"""

x = int(input("Tapez un entier : "))
operation = input("Tapez une opération : ")
y = int(input("Tapez un autre entier : "))

if operation == "+":
    resultat = x + y
    print("Le résultat est de : ", resultat)
elif operation == "-":
    resultat = x - y
    print("Le résultat est de : ", resultat)
elif operation == "/":
    resultat = x / y
    print("Le résultat est de : ", resultat)
elif operation == "*":
    resultat = x * y
    print("Le résultat est de : ", resultat)
