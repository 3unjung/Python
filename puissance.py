def puissance(base, exposant):
    result = 1
    for i in range(exposant):
        result = result * base
    return print(base, '^', exposant, '=', result)


base = int(input('Entree la base du nombre'))
exposant = int(input('Entrez son exposant'))
puissance(base, exposant)



