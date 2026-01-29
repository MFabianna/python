#!/usr/bin/python3

def count_mot(P):
    mot = ""
    nbrM = 0

    P = P + " "   # pour capter le dernier mot

    for i in range(len(P)):
        if P[i] != " ":
            mot = mot + P[i]
        else:
            if mot != "":
                print(mot)
                nbrM = nbrM + 1
                mot = ""

    return nbrM


# -------- PROGRAMME PRINCIPAL --------
P = ""
while P == "":
    P = input("Écrivez une phrase : ")

nb = count_mot(P)
print("Le nombre de mots est :", nb)