import pandas as pd

pd.read_csv("transactions.csv")
df_trans = pd.read_csv("transactions.csv")

pd.read_csv("products.csv")
df_prod = pd.read_csv("products.csv") 

print (df_trans.head(10))

print(df_trans.columns.tolist())

print (df_trans [['NetSales', 'Tax', 'TotalAmount', 'ReceiptNumber', 'Items']])

print (df_trans.isnull().sum())

print (df_trans.duplicated().sum())

print(df_trans["ReceiptNumber"].duplicated().sum())

print (df_trans.dtypes)

df_trans["Date"] = pd.to_datetime(df_trans["Date"])
print (df_trans.dtypes)

print(df_trans.describe())

