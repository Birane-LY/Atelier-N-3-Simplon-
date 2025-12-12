#Demandez à l'utilisateur de saisir le stock initial de prooduits.
#Demandez le nombre de produits vendus aujourd'hui.
#Calculez et affichez le stock restant.
#Si le stock restant est strictement inférieur à 10, affichez le message :
#"Attention : stock faible, penser au réapprovisionnement."

stock_initial = int(input("Entrer le stock inital"))

produits_vendus =int(input("Entrer le nombre de produits vendus"))



while produits_vendus > stock_initial or produits_vendus <0 :
    stock_initial = int(input("Entrer le stock inital"))

    produits_vendus =int(input("Entrer le nombre de produits vendus"))

stock_restant = stock_initial - produits_vendus 


print(f"Il vous reste: {stock_restant}")

if stock_restant < 10: 

    print("Attention: stock faible, penser au reapprovissionnement")
