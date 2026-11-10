import pandas as pd
#charger les deux tableaux NETTOYÉS
trans = pd.read_csv("Data/Transactions_nettoyé.csv")
prod = pd.read_csv("Data/Products_nettoyé.csv")

#reconstruire dans le catalogue, le texte du produit tel qu'il est écrit dans la colonne Items des transactions
def construire_libelle(ligne):
    if ligne["Variant"] == "-":
        return ligne["ProductName"]
    return f'{ligne["ProductName"]} ({ligne["Variant"]})'

#le résultat est rangé dans une nouvelle colonne "Label"
prod["Label"] = prod.apply(construire_libelle, axis=1)
print("Libellés uniques :", prod["Label"].is_unique)
#afficher les 10 premiers libellés
print("10 premiers libellés :")
print(prod[["ProductName","Variant","Label"]].head(10))

#obtenir une ligne par produit vendu
lignes = trans[["ReceiptNumber", "Items"]].copy()
# créer une liste de produits pour chaque ticket
lignes["Label"] = lignes["Items"].str.split(", ")
lignes = lignes.explode("Label")
#Afficher les 10 premières lignes aprés l'explosion
print("10 premières lignes après explosion :")
print(lignes.head(10))

# vérifier que le nombre de produits découpés correspond à la colonne TotalItem
nb_par_ticket = lignes.groupby("ReceiptNumber").size()
total_item = trans.set_index("ReceiptNumber")["TotalItem"]
ecarts = nb_par_ticket != total_item.reindex(nb_par_ticket.index)
print("Tickets où TotalItem est incohérent :", ecarts.sum())

#vérifier que chaque produit vendu existe dans le catalogue.
vendus = set(lignes["Label"])
catalogue = set(prod["Label"])
print("Vendus mais absents du catalogue :", vendus - catalogue)
print("nombre des produits jamais vendus :", len(catalogue - vendus))

#ajouter à chaque produit vendu son ProductId et son prix
lignes = lignes.merge(prod[["Label", "ProductId", "Price"]], on="Label", how="left")
#Afficher les produits du catalogue jamais vendus
print("Produits du catalogue jamais vendus :")
for produit in sorted(catalogue - vendus):
    print("-",produit)
print("Lignes sans ProductId :", lignes["ProductId"].isna().sum())

#comparer la somme des prix du catalogue au montant payé.

# Somme des prix du catalogue pour chaque ticket
somme_prix = lignes.groupby("ReceiptNumber")["Price"].sum()
# Montant réellement payé (TotalAmount)
montant = trans.set_index("ReceiptNumber")["TotalAmount"].reindex(somme_prix.index)
print("Tickets où montant ≠ somme des prix :", (somme_prix != montant).sum())
#Tableau de comparaison entre montant payé et somme des prix
print("Comparaison entre montant payé et somme des prix :")
comparaison = pd.DataFrame({"Montant payé": montant, "Somme des prix": somme_prix})
#Filtrer les tickets où le montant payé est différent de la somme des prix
ecarts_df = comparaison[comparaison["Montant payé"] != comparaison["Somme des prix"]]
#Afficher les 10 premiers tickets avec écart
print("10 premiers tickets avec écart :")
print(ecarts_df.head(10))
print("Classement des tickets avec écart :")
# rien payé (carte de fidélité)
gratuits = (montant == 0).sum()  
# payé moins que le catalogue                                  
remises = ((montant > 0) & (montant < somme_prix)).sum()  
# payé plus que le catalogue         
plus_chers = (montant > somme_prix).sum()                          
print("Gratuits :", gratuits, "| Remises :", remises, "| Plus chers que le catalogue :", plus_chers)

# Si la condition entre assert et la virgule est fausse, le script s'arrête et affiche le message
assert ecarts.sum() == 0, "TotalItem incohérent"
assert len(vendus - catalogue) == 0, "Produits vendus absents du catalogue"
assert lignes["ProductId"].isna().sum() == 0, "Lignes sans ProductId"
assert prod["ProductId"].is_unique, "ProductId en double dans le catalogue"
assert len(lignes) == trans["TotalItem"].sum(), "Lignes ≠ somme de TotalItem"

# Compte les paires (ticket, produit) qui apparaissent plusieurs fois
doublons_paires = lignes.duplicated(subset=["ReceiptNumber", "ProductId"]).sum()
print("Tickets avec le même produit deux fois :", doublons_paires)

# enregistrer la table de liaison Ticket_Produit
lignes[["ReceiptNumber", "ProductId"]].to_csv("Data/Ticket_Produit.csv", index=False)
#Vérification de la somme des TotalItem est coherente avec le nombre de lignes dans Ticket_Produit.csv
print("Somme de TotalItem :", trans["TotalItem"].sum())
print("Ticket_Produit.csv créé :", len(lignes), "lignes")
