import pandas as pd

# Lecture des deux fichiers CSV

df_trans = pd.read_csv("Data/transactions.csv")
df_prod = pd.read_csv("Data/products.csv")

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

print("nettoyage de table Products")

# Supprimer la colonne Description
df_prod = df_prod.drop(columns=["Description"])

# Afficher les 10 premières lignes
print("LES 10 PREMIERES LIGNES")
print(df_prod.head(10))

# Afficher les noms des colonnes
print("LES COLONNES")
print(df_prod.columns.tolist())

# Vérifier les valeurs manquantes
print("VALEURS MANQUANTES")
print(df_prod.isnull().sum())

# Vérifier les lignes dupliquées
print("LIGNES DUPLIQUEES")
print(df_prod.duplicated().sum())

# Vérifier les ProductId dupliqués
print("PRODUCT ID DUPLIQUES")
print(df_prod["ProductId"].duplicated().sum())

# Afficher les types de données
print("TYPES DE DONNEES")
print(df_prod.dtypes)

# Afficher les statistiques descriptives
print("STATISTIQUES DESCRIPTIVES")
print(df_prod.describe())

# Vérifier les valeurs négatives dans Price
print("PRIX NEGATIFS")
print((df_prod["Price"] < 0).sum())

# Vérifier les prix égaux à zéro
print("PRIX EGAUX A ZERO")
print((df_prod["Price"] == 0).sum())

# Afficher les catégories des produits
print("CATEGORIES DES PRODUITS")
print(df_prod["Category"].value_counts())

# Afficher les variantes des produits
print("VARIANTES DES PRODUITS")
print(df_prod["Variant"].value_counts())

# Afficher le nombre de produits par nom
print("NOMBRE DE PRODUITS PAR NOM")
print(df_prod["ProductName"].value_counts())

print("PRODUITS AVEC LE MEME NOM")
print(df_prod[df_prod["ProductName"].duplicated(keep=False)].sort_values("ProductName"))

print("ESPACES AU DEBUT OU A LA FIN")
print(df_prod[
    (df_prod["ProductName"] != df_prod["ProductName"].str.strip()) |
    (df_prod["Variant"] != df_prod["Variant"].str.strip()) |
    (df_prod["Category"] != df_prod["Category"].str.strip())
])

print("LES VARIANTES UNIQUES")
print(df_prod["Variant"].unique())

# Corriger l'erreur dans la colonne Variant
df_prod["Variant"] = df_prod["Variant"].replace(
    "Ice Houesblend",
    "Ice Houseblend"
)

# Vérifier la correction
print("VARIANTES APRES CORRECTION")
print(df_prod["Variant"].unique())

print("PRODUCT NAMES")
print(df_prod["ProductName"].unique())

print("CATEGORIES")
print(df_prod["Category"].unique())