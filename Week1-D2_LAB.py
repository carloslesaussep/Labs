#Q1

amounts = [24.50, 55.00, 120.00, 49.99, 99.50]
for amount in amounts:
    if amount >= 100:
        print("High")
    elif amount >= 50 and amount < 100:
        print("Medium ")
    else:
        print("Low")

#Q2
amount = 124
member = True

if amount >= 100 and member is True:
    print("Discount eligible")
else: 
    print("Not elegible for discount")


#Q3

statuses = [
    "complete",
    "cancelled",
    "complete",
    "complete",
]
 
amounts = [
    45.50,
    18.00,
    62.25,
    30.00,
]

actual_amount = 0
for i in range(len(statuses)):
    if status == "complete":
        actual_amount += amounts[i]

print(f"Total revenue of complete orders: {actual_amount}€")


#Q4

###Correct answe: C

#Q5

for i in range(1, 6):
    print(i)

#Q6

order_ids = [301, 302, 303, 304, 305]
target_id = 303

for order in order_ids:
    if order == target_id:
        break

#Q7

amounts = [45.50, -5.00, 18.00, 0, 62.25]

for amount in amounts:
    if amount <= 0:
        continue
    else:
        print(amount)

#Q8

###Correct answe: A

#Q9

stores = ["London", "Manchester", "Bristol"]

stores.append("Leeds")
print(stores)

stores[stores.index("Bristol")] = "Birmingham"
print(stores)

stores.pop(stores.index("Manchester"))
print(stores)

#Q10

store_ids = ["LDN-01", "MAN-02", "LDN-01", "BRS-03", "MAN-02"]
unique_store_ids = set(store_ids)

print(len(store_ids))
print(len(unique_store_ids))
print(unique_store_ids)

#Q11

store_location = ("LDN-01", "London", "South")

print(store_location[0])
print(store_location[1])
print(store_location[2])

store_location[1] = "Leeds"

#Q12

###Correct answe: D

#Q13

customer_information ={
"customer_id" : "C101",
"name" : "Amelia Clarke",
"city" : "London",
"total_spend" : 425.50
}

print(customer_information["name"])
print(customer_information["total_spend"])

#Q14

all_stores = {
"LDN-01" : {
    "city": "London", 
    "total revenue": "500"
    },
"MAN-02" : {
    "city": "Manchester", 
    "total revenue": "4200"
    }
}
print(all_stores["LDN-01"]["city"])

#Q15

d = {}

cities = ["London", "Manchester", "London", "Leeds", "London", "Manchester"]
for city in cities:
    if city in d:
        d[city] += 1
    else: 
        d[city] = 1

#Q16

###Correct answe: B

#Q17

orders = [
    {"order_id": 401, "city": "London", "amount_gbp": 45.50},
    {"order_id": 402, "city": "Manchester", "amount_gbp": -5.00},
    {"order_id": 401, "city": "London", "amount_gbp": 45.50},
    {"order_id": 403, "city": "Leeds", "amount_gbp": 30.00},
]

accepted_orders = []
rejected_orders = []
seen_ids = set()

for order in orders:
    order_id = order["order_id"]
    
    if order_id in seen_ids or order["amount_gbp"] <= 0:
        rejected_orders.append(order)
    else:
        seen_ids.add(order_id)
        accepted_orders.append(order)

#Q18

x = {}
for order in accepted_orders:
    city = order["city"]
    if city in x:
        x[city] += order["amount_gbp"]
    else:
        x[city] = order["amount_gbp"]

print(x)

#Q19

amounts = [10, -5, 20, 0, 30, 40]
 
valid_count = 0
 
for amount in amounts:
    if amount <= 0:
        continue
 
    print(amount)
    valid_count += 1
 
    if valid_count == 3:
        break

#Q20

# List
# Set (unique values)
# Touple
# Dictionary

