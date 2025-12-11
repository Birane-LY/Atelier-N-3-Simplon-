# Exercice 6 : Boucle et Table de Multiplication 
# Demandez un nombre à l’utilisateur et affichez sa table de multiplication de 1 à 10.

   # Algorithme table_de_multiplication
    # Variables: N, i, resultat: integer
       
  	   # 1. Saisie du nombre N (une seule fois)
try:
	    N = int(input("Veuillez entrer le nombre que vous souhaitez multiplier:"))
except ValueError:
	    print("Erreur : Veuillez saisir un nombre entier.")
	  

	          # 2. Boucle for pour itérer de 1 à 10 (i est le multiplicateur)
for i in range(1, 11): 
	    # Calcul
	    resultat = N * i
	    # Affichage du résultat
print(f"{N} * {i} = {resultat}") 