#1 
print("lab.1")
import pandas as pd
 
source = pd.DataFrame({
    "product_id": [101, 102, 103, 104],
    "price_gbp": ["25.50", "invalid", "12.00", "40.00"],
})

source_cleanse = source[source["price_gbp"] != "invalid"]
source_cleanse["price_gbp"] = pd.to_numeric(source_cleanse["price_gbp"])
print(source_cleanse.dtypes)

#2
print("lab.2")
import pandas as pd
 
source = pd.DataFrame({
    "order_id": [201, 202, 203],
    "amount_gbp": ["45.50", "30.00", "bad"],
})

raw_orders = source
print(raw_orders)
clean_orders = raw_orders[raw_orders["amount_gbp"] != "bad"]
clean_orders["amount_gbp"] = pd.to_numeric(clean_orders["amount_gbp"])
print(clean_orders)

#3
print("lab.3")
print ("1- ETL - Remove the data before it reaches x means data cleansing before load")
print ("2- ELT - Kept raw data request before data processing involves loading before transforming")
print ("3- ETL/ETL - not valid conditions specified for defining ETL or ELT")
print ("4- ETL - Removed before loading is stated")

#4
print("lab.4 - C")

#5
print("lab.5")
batches = {
    "batch_1": [10, 20, 30],
    "batch_2": [40, 50],
    "batch_3": [60, 70, 80],
}

batch_tot = 0
batch_tot_vals = 0
for batch in batches:
    print(batch)
    print(len(batches[batch]))
    batch_tot += 1
    batch_tot_vals += len(batches[batch])

print(f"Total batches: {batch_tot}")
print(f"Total batch item count: {batch_tot_vals}")

#6
print("lab.6")
print("""
1. Batch
2. Streaming
3. Batch
4. Streaming
""")

#7
print("lab.7")

import pandas as pd
 
source = pd.DataFrame({
    "order_id": [301, 302, 303],
    "city": [" London ", None, "Leeds"],
    "amount_gbp": [45.50, 20.00, -5.00],
})

raw_orders = source
clean_orders = raw_orders[raw_orders["city"].notna()]
clean_orders = clean_orders[clean_orders["amount_gbp"] > 0]
clean_orders["city"] = clean_orders["city"].str.strip()
print(clean_orders)

#8
print("lab.8 - A")

#9
print("""
lab.9 
A - Staging
B - Transformation
C - Analytics
D - Staging 
E - Analytics
""")

#10
print("lab.10")

import pandas as pd
 
source = pd.DataFrame({
    "OrderID": [401, 402, 403],
    "CustomerID": [1, 2, 1],
    "Amount": ["45.50", "30.00", "20.00"],
})

source["Amount"] = pd.to_numeric(source["Amount"])

source = source.rename(columns={
    "OrderID": "order_id",
    "CustomerID": "customer_id",
    "Amount": "amount_gbp",
})

print(source)

#11
print("lab.11")

import pandas as pd
 
orders = pd.DataFrame({
    "order_id": [501, 502, 503, 504],
    "city": ["London", "Leeds", "London", "Manchester"],
    "amount_gbp": [45.50, 30.00, 62.25, 50.00],
    "status": ["complete", "complete", "complete", "cancelled"],
})

completed = orders[orders["status"] == "complete"]
completed = completed.groupby("city")["amount_gbp"].sum()
print(f"""Complete orders:
{completed}""")

#12
print("lab.12 - D")

#13
print("""
lab.13
load_source to clean_orders to build_daily_sales to publish_report
""")

#14
print("""
lab.14
Temporary network timeout - Y
Python syntax error - N
Database unavailable for 30 seconds - Y
Required column removed from source file - N
""")

#15
print("""lab.15
Check that the source was updated as planned
Review if any output was generated
Manually run it date by date to spot where the issue may be
Try running the whole code again
""")

#16
print("lab.16 - B")

###Optional exercises
print("Optional Exercises")

#17
print("lab.17")

#18
print("lab.18")

#19
print("lab.19")

#20
print("lab.20")