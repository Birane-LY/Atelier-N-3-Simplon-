# Exercice 2 : Typage Dynamique et Inspection 
# Écrivez un programme Python qui déclare une variable prix_unitaire(décimal) et une variable message (chaîne). Utilisez la fonction type() pour afficher le type de chaque variable, illustrant le typage dynamique de Python.

# Algorithme inspection_python
     # Variables:  prix_unitaire: float ;  message: string
    
    
prix_unitaire = float(input ("Veuillez entrer le prix de l'article que vous souhaitez acheter: "))
print(prix_unitaire)
message = input("Veuillez saisir un commentaire: ")
print(message)
    
         
type(prix_unitaire)
type(message)