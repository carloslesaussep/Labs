#Q1

def calculate_revenue(price, quantity):
    return price*quantity
print(calculate_revenue(3, 2))

#Q2

def calculate_order(unit_price, quantity):
    subtotal = unit_price * quantity
    vat_amount = subtotal * 0.20
    final_total = subtotal + vat_amount

    return {
        "subtotal": subtotal,
        "vat": vat_amount,
        "total": final_total
    }

order = calculate_order(25, 2)

print(order["subtotal"])
print(order["vat"])
print(order["total"])

#Q3

total_orders ={
    "order1": {"unit_price": 10.00, "quantity": 4},
    "order2": {"unit_price": 35.50, "quantity": 2},
    "order3": {"unit_price": 7.25, "quantity": 10},
}

for order_id in total_orders:
    x = total_orders[order_id]["unit_price"]
    y = total_orders[order_id]["quantity"]
    basictouplewithorder = calculate_order(x, y)
    print(
    f"Order id: {order_id} // Subtotal: {basictouplewithorder['subtotal']:.2f} "
    f"// VAT: {basictouplewithorder['vat']:.2f} // Total: {basictouplewithorder['total']:.2f}"
    )
#Q4

### D

#Q5

def apply_discount(amount, discount_percent=5):
    discount = amount*(discount_percent/100)
    return amount-discount 

#Q6

def is_valid_amount(amount):
    if amount > 0:
        return True
    else:
        return False

#Q7

amounts = [100, -10, 50]
for amount in amounts:
    if is_valid_amount(amount) is True:
        print(apply_discount(amount, 10))
    else:
        print("invalid")

#Q8

### B

#Q9

import numpy as np

batch1 = np.array([45.50, 18.00, 62.25])
batch2 =np.array([30.00, 55.50, 12.00])
batch3 =np.array([80.00, 20.00, 100.00])

print(batch_1, batch_1.dtype)
print(batch_2, batch_2.dtype)
print(batch_3, batch_3.dtype)

#Q10

import numpy as np

amounts = np.array([10, 20, 30, 40, 50, 60])
 
print(amounts[0])
print(amounts[-1])
print(amounts[1:4])
print(amounts[:3])

#Q11

import numpy as np

amounts = np.array([45.50, 18.00, 120.00, 62.25, 150.00])
hvs_ = amounts[amounts >= 100]

#Q12

### B

#Q13

import numpy as np

prices = np.array([10.00, 20.00, 50.00])
prices_plus_10 = prices*1.10

#Q14

import numpy as np

sales = np.array([45.50, 18.00, 62.25, 30.00, 55.50])
sales_sum = sales.sum()
sales_min = sales.min()
sales_max = sales.max()
sales_mean = sales.mean()

print(sales_sum)
print(sales_min)
print(sales_max)
print(sales_mean)

#Q15

import numpy as np

sales = np.array([
    [100, 120, 90],
    [80, 110, 105],
    [95, 100, 130],
])

sales_total_per_stpre = sales.sum(axis = 0)
sales_total_per_day = sales.sum(axis = 1)

#Q16

### C

#Q17

import numpy as np

def summarise_sales(x):
    return {
        "total": x.sum(),
        "minimum": x.min(),
        "maximum": x.max(),
        "mean": x.mean(),
    }

#Q18

import numpy as np
 
sales = np.array([45.50, -5.00, 18.00, 0, 62.25])
 
valid_sales = sales[sales > 0]
 
print("Valid values:", valid_sales)
print("Total:", valid_sales.sum())
print("Mean:", valid_sales.mean())

#Q19

##first method
sales = [10, 20, 30, 40, 50]
sales_percent = []
for sale in sales:
    sales_percent.append(sale+(sale*0.1))

print(sales_percent)

##with numpy

import numpy as np
sales = np.array([10, 20, 30, 40, 50])
sales_percent = sales*1.10
print(sales_percent)

#Q20

import numpy as np
 
batch1 = np.array([45.50, 18.00, 62.25])
batch2 =np.array([30.00, 55.50, 12.00])
batch3 =np.array([80.00, 20.00, 100.00])
 
all_sales = np.concatenate([
    batch1,
    batch2,
    batch3,
])
 
average = all_sales.mean()
above_average = all_sales[all_sales > average]
 
print(f"Total:", {all_sales.sum()} Average: {average} Above average: {above_average} Above_average.size)

