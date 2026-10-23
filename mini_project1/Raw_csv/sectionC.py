###Q1

#Get from csvs as read to manipulate wihtin python
import csv
import pandas as pd
import numpy as np

def read_orders(orders_file_path):
    try:
        df_ord = pd.read_csv(orders_file_path)
        
        for _, row in df_ord.iterrows():
            print(
                f"order_id: {row['order_id']}, "
                f"customer_id: {row['customer_id']}, "
                f"product_id: {row['product_id']}, "
                f"order_date: {row['order_date']}, "
                f"quantity: {row['quantity']}, "
                f"unit_price: {row['unit_price']}, "
                f"payment_status: {row['payment_status']}"
            )
        return df_ord  
    except FileNotFoundError:
        print(f"Error: File '{orders_file_path}' not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()


def read_customers(customers_file_path):
    try:
        df_cust = pd.read_csv(customers_file_path)
        
        for _, row in df_cust.iterrows():
            print(
                f"customer_id: {row['customer_id']}, "
                f"customer_name: {row['customer_name']}, "
                f"email: {row['email']}, "
                f"city: {row['city']}, "
                f"signup_date: {row['signup_date']}"
            )
        return df_cust
    except FileNotFoundError:
        print(f"Error: File '{customers_file_path}' not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()


def read_products(products_file_path):
    try:
        df_prod = pd.read_csv(products_file_path)
        
        for _, row in df_prod.iterrows():
            print(
                f"product_id: {row['product_id']}, "
                f"product_name: {row['product_name']}, "
                f"category: {row['category']}, "
                f"supplier_id: {row['supplier_id']}, "
                f"cost_price: {row['cost_price']}, "
                f"selling_price: {row['selling_price']}"
            )
        return df_prod
    except FileNotFoundError:
        print(f"Error: File '{products_file_path}' not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()


def read_clickstream(clickstream_file_path):
    try:
        df_click = pd.read_csv(clickstream_file_path)
        
        for _, row in df_click.iterrows():
            print(
                f"event_id: {row['event_id']}, "
                f"customer_id: {row['customer_id']}, "
                f"event_type: {row['event_type']}, "
                f"page_url: {row['page_url']}, "
                f"event_timestamp: {row['event_timestamp']}, "
                f"device_type: {row['device_type']}"
            )
        return df_click
    except FileNotFoundError:
        print(f"Error: File '{clickstream_file_path}' not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()


clickstream_df = read_clickstream("clickstream.csv")
products_df = read_products("products.csv")
orders_df = read_orders("orders.csv")
customers_df = read_customers("customers.csv")

#Validate schema

import pandas.api.types as ptypes

clickstream_df = clickstream_df.apply(lambda x: x.str.lower().str.strip() if ptypes.is_string_dtype(x) else x)
products_df = products_df.apply(lambda x: x.str.lower().str.strip() if ptypes.is_string_dtype(x) else x)
orders_df = orders_df.apply(lambda x: x.str.lower().str.strip() if ptypes.is_string_dtype(x) else x)
customers_df = customers_df.apply(lambda x: x.str.lower().str.strip() if ptypes.is_string_dtype(x) else x)

#Remove duplicates

def clean_duplicate_customers(df):
    duplicate_rows = df[df.duplicated(subset=['customer_id'], keep='first')]
    
    if not duplicate_rows.empty:
        print(f"Found {len(duplicate_rows)} duplicate customer record(s):")
        print(duplicate_rows)
        print("-" * 40)
    else:
        print("No duplicate customer IDs found.")

    cleaned_df = df.drop_duplicates(subset=['customer_id'], keep='first')
    return cleaned_df

customers_df = clean_duplicate_customers(customers_df)

#Invalid Records

###Q2

#1

customers_df["city"] = customers_df["city"].str.lower()

#2

customers_df["signup_date"] = pd.to_datetime(customers_df["signup_date"], errors='coerce')
orders_df["order_date"] = pd.to_datetime(orders_df["order_date"], errors='coerce')
clickstream_df["event_timestamp"] = pd.to_datetime(clickstream_df['event_timestamp'], errors='coerce')

#3 and 4

def remove_emptyvalue_rows(df):
    initial_count = len(df)
    df = df.replace(r'^\s*$', np.nan, regex=True)
    strict_df = df.dropna(how='any')
    dropped_count = initial_count - len(strict_df)
    print(f"Strict validation: Dropped {dropped_count} rows due to empty values.")
    
    return strict_df

orders_df = remove_emptyvalue_rows(orders_df)
products_df = remove_emptyvalue_rows(products_df)
customers_df = remove_emptyvalue_rows(customers_df)

print(clickstream_df.dtypes)
print(orders_df.dtypes)
print(products_df.dtypes)
print(customers_df.dtypes)

###Q3

#1
print("Most clicks DESC")
ranked_pages = clickstream_df["page_url"].value_counts()


def urlpercentage(df):
    percentages = df['page_url'].value_counts(normalize=True) * 100
    return percentages

url_percentages = urlpercentage(clickstream_df)
print("Percentages:")
print(url_percentages)
print("Total Values:")
print(ranked_pages)

#2
print("Sesion total count")
print(len(clickstream_df))

#3

def mov_vs_desk(df):
    percentages = df['device_type'].value_counts(normalize=True) * 100
    return percentages
mov_vs_dsk_perc = mov_vs_desk(clickstream_df)
print("Percentages:")
print(mov_vs_dsk_perc)