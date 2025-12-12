#Exercice 4 : Condition Simple (Pair ou Impair) 
#Écrivez un programme Python qui demande un nombre à l'utilisateur et affiche s’il est pair ou impair.

#Algorithme Parité
     # Variables:
     # n: integer
      
n = int(input("Veuillez entrer le nombre auquel vous souhaitez vérifier la parité:"))
print(n)
      
if n % 2 == 0 :
    print(f"Le nombre {n} que vous avez saisi est pair")

else:
 print(f"Le nombre {n} que vous avez saisi est impair")