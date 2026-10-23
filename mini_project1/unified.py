import sqlite3
import pandas as pd

conn = sqlite3.connect('project.db')
cursor = conn.cursor()


cursor.execute("DELETE FROM products;")
cursor.execute("DELETE FROM customers;")
cursor.execute("DELETE FROM orders;")
cursor.execute("DELETE FROM clickstream;")
conn.commit()


df_products = pd.read_csv('Raw_csv/products.csv')
df_products.to_sql('products', conn, if_exists='append', index=False)

df_customers = pd.read_csv('Raw_csv/customers.csv')
df_customers.to_sql('customers', conn, if_exists='append', index=False)

df_orders = pd.read_csv('Raw_csv/orders.csv')
df_orders.to_sql('orders', conn, if_exists='append', index=False)

df_clickstream = pd.read_csv('Raw_csv/clickstream.csv')
df_clickstream.to_sql('clickstream', conn, if_exists='append', index=False)

conn.close()

print("CSVs importados - El codigo funciona")