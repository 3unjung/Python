def triangle(n, i = 1):
    if n % 2 == 0:
        print ("Votre nombre n'est pas impair.")
    else:
        while i <= n:
            ligne = "*" * i
            print(ligne.center(n))
            i += 2

for a in range (1):
    n =int(input("Entrer un nombre entier impair : "))
    triangle(n)