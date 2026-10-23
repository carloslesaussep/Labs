import sqlite3
import pandas as pd


columnas = ['product_id', 'product_name', 'category', 'supplier_id', 'cost_price', 'selling_price']
df = pd.read_csv('Raw_csv/products.csv', header=None, names=columnas)
conn = sqlite3.connect('products.db')
df.to_sql('products', conn, if_exists='append', index=False)
conn.close()

print("¡Datos importados con éxito a SQLite!")