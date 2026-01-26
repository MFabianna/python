def compter_voyelles(P):
    voyelles = "aeiouy"

    for v in voyelles:
        nb = P.count(v)
        print("Nombre de", v, ":", nb)

    return P

# Insertion
P = input("Entrez une phrase : ").lower()

# Appel de la fonction
compter_voyelles(P)
