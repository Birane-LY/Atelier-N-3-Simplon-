# Exercice 5 : Boucle for et Somme Cumulative
# Demandez un nombre entier N à l'utilisateur, puis utilisez une boucle pour calculer et afficher la somme de 1+2+3+⋯+N.


   #Algorithme nombre_de_saisie
       #Variables:  i, N, somme: integer
     
     
        # Initialisation de l'accumulateur avant la boucle 
N = 1
somme = 0 
        # Boucle pour répéter la saisie N fois 
for i in range(N+1):

		# Saisie répétée à chaque itération
	N = int(input("Entrez le nombre {i+1} : ")) 
try: 
		# Accumulation de la somme 
	somme = somme + i
		
except ValueError:
		print("Erreur : Veuillez saisir un nombre entier.")

	    # Affichage du résultat final 
print(f"Le résultat de la somme de ces nombres est: {somme}")