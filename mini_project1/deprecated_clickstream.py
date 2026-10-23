import sqlite3
import pandas as pd


columnas = ['event_id', 'customer_id', 'event_type', 'page_url', 'event_timestamp', 'device_type']
df = pd.read_csv('Raw_csv/clickstream.csv', header=None, names=columnas)
conn = sqlite3.connect('clickstream.db')
df.to_sql('clickstream', conn, if_exists='append', index=False)
conn.close()

print("¡Datos importados con éxito a SQLite!")