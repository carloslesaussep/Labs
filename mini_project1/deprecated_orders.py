import sqlite3
import pandas as pd


columnas = ['order_id', 'customer_id', 'product_id', 'order_date', 'quantity', 'unit_price', 'payment_status']
df = pd.read_csv('Raw_csv/orders.csv', header=None, names=columnas)
conn = sqlite3.connect('orders.db')
df.to_sql('orders', conn, if_exists='append', index=False)
conn.close()

print("¡Datos importados con éxito a SQLite!")