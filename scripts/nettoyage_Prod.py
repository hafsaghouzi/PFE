import pandas as pd
df_prod = pd.read_csv("Data/products.csv")

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

#ajout de fichier Products_nettoyé.csv
df_prod.to_csv("Data/Products_nettoyé.csv", index=False)