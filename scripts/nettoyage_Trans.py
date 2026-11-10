import pandas as pd

# Lecture de fichier CSV

df_trans = pd.read_csv("Data/transactions.csv")

print("nettoyage de table Transactions")

# Afficher les 10 premières lignes
print("LES 10 PREMIERES LIGNES")
print(df_trans.head(10))

# Afficher les noms des colonnes
print("LES COLONNES")
print(df_trans.columns.tolist())

# Afficher quelques colonnes importantes
print("COLONNES IMPORTANTES")
print(df_trans[['NetSales', 'Tax', 'TotalAmount', 'ReceiptNumber', 'Items']])

# Vérifier les valeurs manquantes
print("VALEURS MANQUANTES")
print(df_trans.isnull().sum())

# Vérifier les lignes dupliquées
print("LIGNES DUPLIQUEES")
print(df_trans.duplicated().sum())

# Vérifier les numéros de reçus dupliqués
print("RECEIPT NUMBER DUPLIQUES")
print(df_trans["ReceiptNumber"].duplicated().sum())

# Afficher les types de données
print("TYPES DE DONNEES")
print(df_trans.dtypes)

# Convertir la colonne Date en format datetime
df_trans["Date"] = pd.to_datetime(df_trans["Date"])

print("TYPES DE DONNEES APRES CONVERSION")
print(df_trans.dtypes)

# Afficher les statistiques descriptives
print("STATISTIQUES DESCRIPTIVES")
print(df_trans.describe())

# Afficher les transactions avec des montants égaux à zéro
print("TRANSACTIONS AVEC MONTANT ZERO")
print(df_trans[
    (df_trans["NetSales"] == 0) |
    (df_trans["TotalAmount"] == 0)
])

# Compter les transactions avec un montant égal à zéro
print("NOMBRE DE TRANSACTIONS AVEC MONTANT ZERO")
print((df_trans["TotalAmount"] == 0).sum())

# Calculer le pourcentage des transactions avec montant zéro
print("POURCENTAGE DES TRANSACTIONS AVEC MONTANT ZERO")
print((df_trans["TotalAmount"] == 0).mean() * 100)

# Créer un DataFrame contenant les transactions avec montant zéro
zero_sales = df_trans[df_trans["TotalAmount"] == 0]

# Vérifier NetSales et Tax pour ces transactions
print("NETSALES ET TAX DES TRANSACTIONS ZERO")
print(zero_sales[["NetSales", "Tax"]].value_counts())

# Vérifier les méthodes de paiement
print("METHODES DE PAIEMENT DES TRANSACTIONS ZERO")
print(zero_sales["PaymentMethod"].value_counts())

# Vérifier l'utilisation de la carte de fidélité
print("CARTE DE FIDELITE DES TRANSACTIONS ZERO")
print(zero_sales["UseLoyaltyCard"].value_counts())

# Afficher le nombre d'utilisations de la carte de fidélité
print("UTILISATION DE LA CARTE DE FIDELITE")
print(df_trans["UseLoyaltyCard"].value_counts())

# Comparer la carte de fidélité avec les montants zéro
print("CARTE DE FIDELITE ET MONTANT ZERO")
print(pd.crosstab(df_trans["UseLoyaltyCard"], df_trans["TotalAmount"] == 0))

# Vérifier les valeurs négatives
print("VALEURS NEGATIVES DE NETSALES")
print((df_trans["NetSales"] < 0).sum())

print("VALEURS NEGATIVES DE TAX")
print((df_trans["Tax"] < 0).sum())

print("VALEURS NEGATIVES DE TOTALAMOUNT")
print((df_trans["TotalAmount"] < 0).sum())

# Vérifier la cohérence entre TotalAmount, NetSales et Tax
print("VERIFICATION DU TOTAL")
print((df_trans["TotalAmount"] != df_trans["NetSales"] + df_trans["Tax"]).sum())

# Vérifier les quantités d'articles
print("QUANTITES D'ARTICLES INFERIEURES OU EGALES A ZERO")
print((df_trans["TotalItem"] <= 0).sum())

# Afficher le nombre de transactions par quantité d'articles
print("NOMBRE D'ARTICLES PAR TRANSACTION")
print(df_trans["TotalItem"].value_counts())

# Afficher les 10 premières valeurs de Items
print("LES 10 PREMIERES VALEURS DE ITEMS")
print(df_trans["Items"].head(10))

# Vérifier les méthodes de paiement
print("METHODES DE PAIEMENT")
print(df_trans["PaymentMethod"].value_counts())

# Vérifier les points de vente
print("NOMBRE DE TRANSACTIONS PAR OUTLET")
print(df_trans["Outlet"].value_counts())

# Afficher les 10 premières heures
print("LES 10 PREMIERES HEURES")
print(df_trans["Time"].head(10))

# Vérifier le format de la colonne Time
print("HEURES AVEC FORMAT INCORRECT")
print(pd.to_datetime(df_trans["Time"], format="%H:%M:%S", errors="coerce").isnull().sum())

# Corriger l'erreur dans la colonne Items
print("Lignes avec la faute :", df_trans["Items"].str.contains("Houesblend").sum())
df_trans["Items"] = df_trans["Items"].str.replace("Houesblend", "Houseblend")
print("Lignes avec la faute après correction :", df_trans["Items"].str.contains("Houesblend").sum())

# Découpage du numéro de ticket en 3 morceaux
ticket_outlet = df_trans["ReceiptNumber"].str[:7]    # 7 premiers caractères : le point de vente
ticket_mois = df_trans["ReceiptNumber"].str[7:10]    # les 3 suivants : le mois (JAN, FEB...)
ticket_annee = df_trans["ReceiptNumber"].str[10:12]  # les 2 suivants : l'année (25)

# Nombre de tickets dont le point de vente du numéro ≠ colonne Outlet. Attendu : 0
print("Outlet incohérent :", (ticket_outlet != df_trans["Outlet"]).sum())

# Nombre de tickets dont l'année du numéro ≠ année de la date. Attendu : 0
print("Année incohérente :", (ticket_annee != df_trans["Date"].dt.strftime("%y")).sum())

# Tableau croisé mois du numéro / mois de la date
print("Tableau croisé mois du numéro / mois de la date")
print(pd.crosstab(ticket_mois, df_trans["Date"].dt.month))

# Même point de vente, même date, même heure, mêmes produits, même montant, mais un numéro de ticket différent
colonnes_test = ["Outlet", "Date", "Time", "Items", "TotalAmount"]
print("Tickets quasi identiques :", df_trans.duplicated(subset=colonnes_test).sum())

# on exclut les tickets gratuits (division par 0)
payants = df_trans[df_trans["NetSales"] > 0]   
# taux de taxe de chaque ticket     
taux = payants["Tax"] / payants["NetSales"]          
print("Taux min et max :", taux.min(), taux.max())
print("Tickets payants contrôlés :", len(payants))
print("Tickets dont le taux n'est pas de 11 % :", (~taux.between(0.109, 0.111)).sum())

# Nombre de jours entre la première et la dernière date inclus
nb_jours = (df_trans["Date"].max() - df_trans["Date"].min()).days + 1
print("Jours dans la période :", nb_jours)
# Jours avec au moins une vente, pour chaque point de vente
print("Jours avec au moins une vente par point de vente :")
print(df_trans.groupby("Outlet")["Date"].nunique())
# Première et dernière heure de vente de chaque point de vente
print("Première et dernière heure de vente par point de vente :")
print(df_trans.groupby("Outlet")["Time"].agg(["min", "max"]))

#ajout de fichier Transactions_nettoyé.csv
df_trans.to_csv("Data/Transactions_nettoyé.csv", index=False)
