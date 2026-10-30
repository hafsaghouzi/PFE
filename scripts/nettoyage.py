import pandas as pd

df_trans = pd.read_csv("Data/transactions.csv")

df_prod = pd.read_csv("Data/products.csv") 

print (df_trans.head(10))

print(df_trans.columns.tolist())

print (df_trans [['NetSales', 'Tax', 'TotalAmount', 'ReceiptNumber', 'Items']])

print("Nombre des valeurs manquantes")
print (df_trans.isnull().sum())

print("Nombre des valeurs dupliquées")
print (df_trans.duplicated().sum())

print("Nombre de reçus dupliqués:")
print(df_trans["ReceiptNumber"].duplicated().sum())

print (df_trans.dtypes)
#Convertir la colonne "Date" en type datetime
df_trans["Date"] = pd.to_datetime(df_trans["Date"])
print (df_trans.dtypes)
#Afficher les statistiques descriptives pour les colonnes numériques
print(df_trans.describe())
print("Transactions avec NetSales ou TotalAmount égale à zéro:")
print(df_trans[
    (df_trans["NetSales"] == 0) |
    (df_trans["TotalAmount"] == 0) 
])
print("Nombre de transactions dont le TotalAmount est égal à zéro:")
print((df_trans["TotalAmount"] == 0).sum())
print("Pourcentage de transactions dont le TotalAmount est égal à zéro:")
print((df_trans["TotalAmount"] == 0).mean() * 100)
#Créer un DataFrame contenant uniquement les transactions avec TotalAmount égal à zéro
zero_sales = df_trans[df_trans["TotalAmount"] == 0]
print("Nombre d'occurrences de chaque combinaison de NetSales et Tax pour les transactions avec TotalAmount égal à zéro:")
print(zero_sales[["NetSales", "Tax"]].value_counts())
#Identifier les méthodes de paiement et l'utilisation de la carte de fidélité pour les transactions avec TotalAmount égal à zéro
print(zero_sales["PaymentMethod"].value_counts())
print(zero_sales["UseLoyaltyCard"].value_counts())
print("Nombre de transactions avec et sans carte de fidélité")
print(df_trans["UseLoyaltyCard"].value_counts())
print("Tableau croisé entre l'utilisation de la carte de fidélité et le TotalAmount égal à zéro")
print(pd.crosstab(df_trans["UseLoyaltyCard"], df_trans["TotalAmount"] == 0))
print("Nombre de transactions avec NetSales négatif:")
print((df_trans["NetSales"] < 0).sum())