factoriel = 1 
n = int(input("Tapez un entier pour connaître son factoriel : "))
for i in range(1,n*1): 
    factoriel = factoriel * i # multiplie factoriel * chaque tour de la boucle
    print("La factorielle est de :", factoriel)