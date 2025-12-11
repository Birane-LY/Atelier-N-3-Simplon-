# Exercice 10 : Fonctions et Portée des Variables 
# Écrivez un programme qui définit une variable global_data dans le corps principal. Définissez une fonction et utilisez le mot-clé global pour modifier la valeur de global_data à l'intérieur de cette fonction. Expliquez le comportement.

# Définition de la variable globale dans le corps principal
global_data = 50 
print(f"Valeur initiale de global_data : {global_data}")

# Définition de la fonction qui va modifier la variable globale
def ModifierGlobale(ajout):
    # Utilisation du mot-clé global pour indiquer à Python que nous manipulons
    # la variable 'global_data' définie en dehors de cette fonction.
    global global_data # Déclare l'intention de modifier la variable globale 
    
    # Modification de la variable globale
    global_data = global_data + ajout
    print(f"Valeur de global_data dans la fonction après modification : {global_data}")

# Appel de la fonction
ModifierGlobale(75)

# Vérification dans le corps principal après l'appel
print(f"Valeur finale de global_data dans le corps principal est: {global_data} ")