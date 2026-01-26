n = int(input("Entrer un nombre : ")) # lecture du nombre

fact = 1 # initialisation

for i in range(1, n + 1): # de 1 jusqu’à n
    fact = fact * i # multiplication

print("Le factoriel est :", fact) # affichage
