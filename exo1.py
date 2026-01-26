Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> semaine=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
>>> semaine=[0:5]
SyntaxError: invalid syntax
>>> semaine[0:5]
['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
>>> KeyboardInterrupt
>>> semaine[5:7]
['Samedi', 'Dimanche']
>>> semaine[6]
'Dimanche'
>>> semaine[-1]
'Dimanche'
>>> semaine.reverse()
>>> semaine
['Dimanche', 'Samedi', 'Vendredi', 'Jeudi', 'Mercredi', 'Mardi', 'Lundi']
>>> semaine.reverse()
>>> semaine
['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
>>> semaine.sort(reverse=True)
>>> semaine
['Vendredi', 'Samedi', 'Mercredi', 'Mardi', 'Lundi', 'Jeudi', 'Dimanche']
>>> semaine=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
>>> semaine.sort(reverse="True")
>>> semaine
['Vendredi', 'Samedi', 'Mercredi', 'Mardi', 'Lundi', 'Jeudi', 'Dimanche']
>>> semaine=["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
>>> KeyboardInterrupt
>>> semaine[-7:-2]
['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
>>> semaine[-2:7]
['Samedi', 'Dimanche']
>>> semaine[-2:]
['Samedi', 'Dimanche']
