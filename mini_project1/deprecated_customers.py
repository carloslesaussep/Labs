import sqlite3
import pandas as pd


columnas = ['customer_id', 'customer_name', 'email', 'city', 'signup_date']
df = pd.read_csv('Raw_csv/customers.csv', header=None, names=columnas)
conn = sqlite3.connect('customers.db')
df.to_sql('customers', conn, if_exists='append', index=False)
conn.close()

print("¡Datos importados con éxito a SQLite!")