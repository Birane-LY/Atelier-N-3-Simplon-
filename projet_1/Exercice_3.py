#Demandez à l'utilisateur de saisir 10 nombres (positifs ou négatifs).
#Créez une nouvelle liste qui contient uniquement les nombres supérieurs ou égaux à 0
#(nombres non négatifs).Affichez la nouvelle liste.

Liste =[]
List = []

List_1 = []

for i in range(1,11) :

    nombre = float(input("Veuillez entrer les nombres"))

    List.append(nombre)
    if nombre >= 0 :

      List_1.append(nombre)

    else :
       print("Le nombre est negatif") 

print(f"la lsite des nombres positifs est:{List_1}")
print(f"La liste des dix nombres est:{List}")



