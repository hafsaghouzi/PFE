import pandas as pd

df_trans = pd.read_csv("Data/transactions.csv")

df_prod = pd.read_csv("Data/products.csv") 

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

print(df_trans[
    (df_trans["NetSales"] == 0) |
    (df_trans["TotalAmount"] == 0) 
])
print((df_trans["TotalAmount"] == 0).sum())
print((df_trans["TotalAmount"] == 0).mean() * 100)
zero_sales = df_trans[df_trans["TotalAmount"] == 0]
print(zero_sales[["NetSales", "Tax"]].value_counts())
print(zero_sales["PaymentMethod"].value_counts())
print(zero_sales["UseLoyaltyCard"].value_counts())
print(df_trans["UseLoyaltyCard"].value_counts())
print(pd.crosstab(df_trans["UseLoyaltyCard"], df_trans["TotalAmount"] == 0))

print((df_trans["NetSales"] < 0).sum())