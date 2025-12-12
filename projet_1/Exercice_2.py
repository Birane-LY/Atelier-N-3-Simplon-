#Deandez 3 nombres à l’utilisateur pour constituer une première liste (Liste A).
#Demandez 3 autres nombres à l’utilisateur pour constituer une deuxième liste (Liste B).
#Créez une troisième liste (Liste C) qui contient tous les éléments de la Liste A suivis
#de tous les éléments de la Liste B.
#Affichez la Liste C.


liste_A = []

liste_B = []

liste_C = []

print(f"remplir la liste A")

for i in range(1,4):

    nombre = int(input("Entrer un nombre"))

    liste_A.append(nombre)

   
print("remplir la liste B")

for i in range(1,4) :

    nbre = int(input("Veuillez entrer un nombre"))
    
    liste_B.append(nbre)

liste_C.extend(liste_A)
liste_C.extend(liste_B)

print(f"La liste C est: {liste_C}")
