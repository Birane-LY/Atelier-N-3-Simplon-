# Exercice 7 : Boucle while et Authentification 
# Le mot de passe correct est "python123". L'utilisateur dispose de 3 tentatives pour saisir ce mot de passe. Utilisez une boucle while pour gérer les tentatives et afficher un message de succès ou d'échec

   # Algorithme mot_de_passe
     # Variables: tentative : integer ; mdp: string
      
tentative = 1  
mdp = "python123"

            # Saisie et conversion en entier (
mdp = input("Veuillez entrer votre mot de passe:")
print(mdp)

            # La boucle continue tant que le décompte est supérieur ou égal à 1
while tentative <= 2 and mdp != "python123": 
                tentative += 1
                print(tentative)
                mdp = input("Veuillez entrer votre mot de passe:")
                print(mdp)
                
            # Incrémenter la variable pour avancer vers la fin de la boucle
if tentative == 3   :
            # Affichage final après la sortie de la boucle 
            print("Votre mot de passe est correct.")
else :
                
            print("Votre mot de passe est incorrect et vous avez atteint votre nombre de tentatives")

	