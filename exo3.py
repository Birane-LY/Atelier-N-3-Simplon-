# Exercice 3 : Opérations et Entrée Utilisateur
# Écrivez un programme Python qui demande deux nombres à l’utilisateur et affiche : leur addition, soustraction, multiplication et division.

 # Algorithme calculatrice
     # variables:
     # A, B, somme, difference, produit, quotient: float
     # Entrée Utilisateur

A = float(input("Veuillez entrer le premier nombre: "))
print(A)
      
B = float(input("Veuillez entrer le deuxième nombre: "))
print(B)
      
try:
       # 1. Calcul des opérations
    somme = A + B
    difference = A - B
    produit = A * B
    
    # Gestion de la division par zéro avant le calcul
    if B != 0:
        quotient = A / B
    else:
        quotient = "Division par zéro impossible"
    
    # 2. Affichage des résultats 
    print(f"Addition (A + B) : {somme}")
    print(f"Soustraction (A - B) : {difference}")
    print(f"Multiplication (A * B) : {produit}")
    print(f"Division (A / B) : {quotient}")

except : 
    # (si l'utilisateur ne saisit pas un nombre) 
    print("Erreur de type : Veuillez saisir uniquement des chiffres pour les nombres.") 
