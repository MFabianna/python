def factoriel(n): #appel du fontion 
    fact = 1 # initialisation par 1

    for i in range(1, n + 1): # de 1 jusqu’à n
        fact = fact * i # multiplication

    return fact #renvoie du résultat
    
#Insertion et affichage     
n = int(input("Entrer un nombre : "))
res = factoriel(n)
print("Le factoriel", n, "est :", res)
