# Exercice 9 : Statistiques de Base sur une Liste 
# À partir d'une liste de 5 nombres (que vous pouvez définir ou demander à l'utilisateur), affichez : la somme, la moyenne, le maximum et le minimum, en utilisant les fonctions intégrées de Python.

# Algorithme statistique 
# variables: i, n, somme, moyenne, maximum, minimum: float

# Initialisation de la liste pour stocker les nombres
liste_nombres = [] 
NOMBRE_ELEMENTS = 5 

try:
    # 1. Collecte des 5 nombres et stockage dans la liste
    for i in range(NOMBRE_ELEMENTS): 
        # Répétition de la saisie 
        nombre = float(input(f"Entrez le nombre {i+1} : ")) 
        liste_nombres.append(nombre) 
    # 2. Calcul des statistiques après la boucle
    
    # Utilisation des fonctions intégrées 
    somme = sum(liste_nombres)
    moyenne = somme / NOMBRE_ELEMENTS
    maximum = max(liste_nombres)
    minimum = min(liste_nombres)

    # 3. Affichage des résultats
    print(f"Liste des nombres saisis : {liste_nombres}")
    print(f"Somme : {somme}")
    print(f"Moyenne : {moyenne}")
    print(f"Maximum : {maximum}")
    print(f"Minimum : {minimum}")

except ValueError: 
    print("Erreur de format : Veuillez saisir uniquement des nombres.")
