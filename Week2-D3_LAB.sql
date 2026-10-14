# Q1
customer
    customer_id PK
    customer_name
    customer_city
order
    order_id PK
    customer_id FK
    order_date
product
    product_id PK
    product_name
    unit_price_gbp
order_item
    order_id FK
    product_id FK
    quantity

#Q2
customer --> orders (customer with many order_ids)
order --> products (order with many product_ids)
product --> orders (many orders with same product_ids)

#Q3
CREATE TABLE customers(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(20) NOT NULL,
    customer_city VARCHAR(30) NOT NULL
);

CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(20) NOT NULL,
    unit_price_gbp DECIMAL(10,2) NOT NULL
);

CREATE TABLE order_item(
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

#Q4 C

#Q5
the problem comes from products having multiple values stored within it.
order_id    customer_id     products
101         1               p1
101         1               p2
102         2               p3

#Q6
the problem is that multiple products can be stored within a single order
product_id should be stored with product_name, and the other 2 could be stored wuth product id for orders

#Q7
the city is not tied directly to the customer, but rather to the postcode. Many customers may have repeated pcs, so the city value is undermined and does not bring relevancy to the table.

#Q8 B

#Q9
INSERT INTO customers VALUES
(1, 'Amelia Clarke', 'London'),
(2, 'Oliver Bennett', 'Manchester');
 
INSERT INTO products VALUES
(10, 'Desk Lamp', 25.00),
(11, 'Office Chair', 80.00),
(12, 'Notebook Set', 10.00);
 
INSERT INTO orders VALUES
(1001,'2026-08-01', 1),
(1002, '2026-08-01', 2),
(1003, '2026-08-02', 1);
 
INSERT INTO order_items VALUES
(1001, 10, 2),
(1001, 12, 1),
(1002, 11, 1),
(1003, 12, 3);

SELECT o.order_id, o.order_date, c.customer_name, c.customer_city, p.product_name, oi.quantity, p.unit_price_gbp, oi.quantity * p.unit_price_gbp AS line_total_gbp FROM orders AS o
JOIN customers AS c ON o.customer_id = c.customer_id
JOIN order_items AS oi ON o.order_id = oi.order_id
JOIN products AS p ON oi.product_id = p.product_id

#Q11 A

#Q12 D

#Q13
FACTS: date, cistomer_id, product_id, store_id, quantity, sales_gbp
DIMENSIONS: customer_name, product_name, store_name

#Q14 B to keep clear the products oredered per order, otherwise we would lack the info keeping 1 lane per order

#Q15

                DIM DATE
    DIM CX                      DIM PROD
                FACTSALES
               
                DUN STORE

#Q16 A

#Q17
orders: order_id PK, order_date, customer_id FK, 
customers: customer_id PK, name, customer_city
products: product_id PK, product_name, unit_price_gbp
order_placement: order_id FK, product_id FK, quantity, unit_price_gbp

#Q18 dont understand the problem**

#Q19

FactSALES 
    DimCustomer
        c_id
        c_name
        c_city
    DimProducts 
        p_id
        p_name
        p_unit_price
    DimOrders
        order_id    
        c_id
        o_date
    DimOrder_placements
        o_id
        p_id
        p_quant
        price_overall


#Q20

    1. Single event entry
    2. keys
    3. duplicates (?)
    4. atributes
    5. FKs need to keep the values according to PKs
    6. OLTP due to being normalized
