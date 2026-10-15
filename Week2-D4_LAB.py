#1

1. DL - 
2. DW - Structured with sql usage
3. LH - Table usage and flexible storage
4. DL - Raw unstructured sotrage

#2

1. Any non WH - Assumed to be overall files so nondefined quantity nor timeline, thus not fitted for wh
2. Any non WH - Assumed to be overall files so nondefined quantity nor timeline, thus not fitted for wh
3. Any non WH - Assumed to be overall files so nondefined quantity non timeline, thus not fitted for wh
4. WH - Tied to short and specific timeline
5. WH - Tied to short and specific timeline

#3
                                    Data lake           Data Warehouse          Lakehouse
Raw data support                    yes                 conversion of raw data  yes
Strong structured reporting         flexible            yes                     yes
Flexible data shapes                yes                 not at all              yes
Table-style analytics               not necesarily      yes                     yes

#4 D

#5

A. Read
B. Write
C. Write
D. Write

#6

1. Bronze: all raw data shall be kept
2. Silver: data after reviewed for non duplicate order ids, removed negative amount_gbp, etc.

#7

import pandas as pd

batch1 = pd.DataFrame(
        [(101, "london", 45.50, "complete"),
        (102, "manchester", -5, "complete")],
    columns = ["order_id", "city", "price", "status"]
)

batch2 = pd.DataFrame(
        [(103, "bristol", 30.00, "complete"),
        (104, "leeds", 20, "cancelled")],
    columns = ["order_id", "city", "price", "status"]
)

batch3 = pd.DataFrame(
        [(103, "london", 45.50, "complete"),
        (104, "manchester", 51, "complete")],
    columns = ["order_id", "city", "price", "status"]
)

bronze_batches = pd.concat([batch1, batch2, batch3], ignore_index=True)
print("bronze")
print(bronze_batches)
first_cleanse =  bronze_batches[bronze_batches["price"] >= 0]
second_cleanse = first_cleanse.drop_duplicates(subset=["order_id"])
third_cleanse = second_cleanse
third_cleanse["city"] = third_cleanse["city"].str.strip()
third_cleanse = silver_batches
print(silver_batches)
print(silver_batches)

#8 C

#9

gold_complete = silver_batches[silver_batches["status"] == "complete"]
gold_summary_city = silver_batches.groupby("city")["price"].sum
gold_summary_city_sorted = gold_summary_city.sort_values(by="price", ascending = False)
print("gold summary with complete orders")
print(gold_complete)
print("gold summary grouped cities")
print(gold_summary_city)
print("gold summary sorted group cities")
print(gold_summary_city_sorted)

#10
1. Structured
2. Semi-structured
3. Structured
4. Unstructured
5. Unstructured

#11 ?

#12 A

#13 
 
A. Storage
B. Compute
C. Storage
D. Compute

#14 ?

#15

            purpouse            main col            source                  own/team            lastknownupdate
bronz       raw untreated data                      raw input into table    eng                 eng
silv        cleansed data                           treated bronze cleanse  eng                 eng
gold        data ready for                          diverted silver         data science        ds da
            analysis

#16 B

#extras

#17

#18

#19 Correct: Total invalid rows are 40, thus 1000-40 = silver rows

#20