nombre = input('Tapez  entier positif : ')

nombre = int(nombre)

print('Le programme est en train de vérifier si ce nombre est premier...')

i = 2

while i < nombre and nombre % i != 0 :

    i = i + 1

if i == nombre :

    print('Le nombre', nombre, 'est premier !')

else :

    print('Ce n\'est pas un nombre premier.')