#Q1

order_id = 1001
city = London
amount_gbp = 45.50
is_complete = True
print(order_id)
print(city)
print(amount_gbp)
print(is_complete)

#Q2

order_id = 1002
city = Manchester
amount_gbp = 18.00
is_complete = False
print(f"Order {order_id} from {city} has a value of {amount_gbp}")

#Q3

store_name = "Bristol"
print(f"Store: {store_name}")

#Q4

###Right answer is B

#Q5

order_count = 12
average_value = 36.75
store_name = "Leeds"
is_open = True
print(type(order_count))
print(type(average_value))
print(type(store_name))
print(type(is_open))

#Q6

unit_price = 24.50
quantity = 3
delivery_fee = 4.99

subtotal = float(unit_price*quantity)
final_total = float(subtotal*delivery_fee)
print(round(subtotal, 2))
print(round(final_total, 2))

#Q7

quantity_text = "4"
price_text = "12.50"
transformed_quantity = int(quantity_text)
transformed_price = float(price_text)

total = transformed_quantity*transformed_price
print(total)

#Q8

###Right answer is D

#Q9

x = int(input("Enter second value: "))
is_high_value = x >= 100
print("High value:", is_high_value)

#Q10
def order_acceptance(status, amount_gbp):
    if status == "complete" and amount_gbp > 0:
        print(True)
        return True
    else:
        print(False)
        return False

print("case 1")
order_acceptance("complete", 45.50)
print("case 2")
order_acceptance("cancelled", 45.50)
print("case 3")
order_acceptance("complete", -5.00)

#Q11

store_name = input("Store name: ")
amount_gbp = float(input("Order amount: "))
is_accepted = amount_gbp > 0
 
print(f"{store_name} order accepted: {is_accepted}")

#Q12

###Right answer is A

#Q13

city = London
orders = 8
revenue_gbp = 356.7

print(f"{city}: {orders} orders | Revenue: £{revenue_gbp}")

#Q14
####A - Second quote
city = "London"
print(city)
####B - variable name in print command
amount = 25
print(amount)
####C - quotes for it not to be set as a string (could also be used float to change the preset of the variable)
amount = 25
print(amount + 10)
####D - "three" not valid
quantity = int(3)

#Q15

amount = 125
print(amount)

#Q16

###Right answer is C

#Q17

order_id = input("Enter order ID: ")
city = input("Enter city: ")
unit_price = input("Enter unit price: ")
quantity = input("Enter item ammount: ")
discount_percent = input("Enter discount ammount: ")

subtotal = float(float(unit_price)*int(quantity))
discount_amount = subtotal*(int(discount_percent)/100)
final_amount = subtotal - discount_amount
print(f"""
Subtotal: {subtotal}
Discount ammount: {discount_amount}
Final ammount: {final_amount}
""")

#Q18

quantity = int(input("Quantity: "))
discount_percent = float(input("Discount %: "))
 
valid_quantity = quantity > 0
valid_discount = (discount_percent >= 0 and discount_percent <= 100)
all_valid = valid_quantity and valid_discount
 
print("Valid quantity:", valid_quantity)
print("Valid discount:", valid_discount)
print("All values valid:", all_valid)

#Q19

city = input("City: ")
amount = float(input("Amount: "))
 
is_high_value = amount >= 100
 
print(
    f"{city} | £{amount:.2f} | "
    f"High value: {is_high_value}"
)

#Q20

value = input("Enter value")
high_value_check = float(value) >= 100
print(high_value_check)
###Testing 100.00 is important to review wether it is considering decimals