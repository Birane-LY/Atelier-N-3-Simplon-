# Exercice 8 : Introduction aux Listes 
# Demandez 5 nombres à l’utilisateur et stockez-les dans une liste. Affichez ensuite les éléments de la liste un par un.

  # Variables : NOMBRE_ELEMENTS: integer, nombre: float
# La liste 'liste_nombres' stockera les entrées (tableau en algorithmique)

NOMBRE_ELEMENTS = 5
liste_nombres = [] # Initialisation de la liste (tableau)

# 1. Saisie des 5 nombres et stockage
print(f"Veuillez entrer {NOMBRE_ELEMENTS} nombres.")

# Utilisation d'une boucle 'for' pour répéter 5 fois la saisie 
for i in range(NOMBRE_ELEMENTS): 
    try:
        # Saisie et conversion en nombre décimal (float) 
        nombre = float(input(f"Entrez le nombre {i+1} : ")) 
        liste_nombres.append(nombre) # Ajout du nombre à la liste
        
    except ValueError:
        # Gestion de l'erreur si l'entrée n'est pas un nombre [6]
        print("Erreur de format: Veuillez entrez uniquement des chiffres.")

# 2. Affichage des éléments un par un

print("\n--- Les nombres de la liste sont : ---")
# Boucle for pour itérer sur les éléments de la liste
for element in liste_nombres:
    print(liste_nombres)
    break

print("Fin de l'affichage.")
  