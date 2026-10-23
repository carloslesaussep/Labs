-- base para establecer customers con PKs luego accionar codigo
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    email VARCHAR(50),
    city VARCHAR(30),
    signup_date DATE
);

-- base para establecer products con PKs luego accionar codigo 
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(30),
    category VARCHAR(30),
    supplier_id INT,
    cost_price DECIMAL (20,2),
    selling_price DECIMAL (20,2)
);

-- base para establecer orders con PKs luego accionar codigo  [FKs customers y products respective IDs]
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    unit_price DECIMAL (20,2), 
    payment_status VARCHAR (30), 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- base para establecer clickstream
CREATE TABLE IF NOT EXISTS clickstream(
    event_id INT,
    customer_id INT,
    event_type VARCHAR (30),
    page_url VARCHAR (30),
    event_timestamp DATETIME, 
    device_type VARCHAR (30),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- checkear si se mantienen PKs
PRAGMA table_info(orders);
PRAGMA table_info(customers);
PRAGMA table_info(products);
PRAGMA table_info(clickstream);


--Q1.1
SELECT c.customer_id, c.customer_name, (o.quantity*o.unit_price) AS total_spent
FROM customers AS c
LEFT JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 10;

--Q1.2
WITH monthly_sales AS (
    SELECT strftime('%Y-%m', order_date) AS sales_month, SUM(unit_price * quantity) AS total_revenue
    FROM orders
    GROUP BY sales_month
)

SELECT sales_month, total_revenue, COALESCE(LAG(total_revenue) OVER (ORDER BY sales_month), 0) AS prev_month_revenue, COALESCE(total_revenue - LAG(total_revenue) OVER (ORDER BY sales_month), 0) AS MoM_Revenue
FROM monthly_sales;

--Q1.3

--Q1.4
SELECT p.product_id, p.category, COALESCE(SUM(o.quantity), 0) AS total_quantity
FROM products AS p
LEFT JOIN orders AS o ON p.product_id = o.product_id
GROUP BY p.product_id
HAVING COALESCE(SUM(o.quantity), 0) = 0;

--Q1.5
SELECT p.category, COALESCE(SUM(o.quantity), 0) AS ordered_amount, COALESCE(SUM(o.quantity)*cost_price, 0) AS total_revenue
FROM products AS p
LEFT JOIN orders AS o ON p.product_id = o.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;

--Q2.1
SELECT c.customer_id, c.customer_name, (o.quantity*o.unit_price) AS total_spent
FROM customers AS c
LEFT JOIN orders AS o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC;

--Q2.2


--Q2.3
SELECT p.category, p.product_id, p.product_name, COALESCE(SUM(o.quantity * o.unit_price), 0) AS total_sold
FROM products AS p
LEFT JOIN orders AS o ON p.product_id = o.product_id
GROUP BY p.category, p.product_id
ORDER BY total_sold DESC;

WITH ranked_products AS (
    SELECT p.category, p.product_id, p.product_name, COALESCE(SUM(o.quantity * o.unit_price), 0) AS total_sold, ROW_NUMBER() OVER (PARTITION BY p.category ORDER BY COALESCE(SUM(o.quantity * o.unit_price), 0) DESC) AS rank1
    FROM products AS p
    LEFT JOIN orders AS o ON p.product_id = o.product_id
    GROUP BY p.category, p.product_id
)
SELECT category, product_id, product_name AS top_products, total_sold
FROM ranked_products
WHERE rank1 = 1;

--Q2.4
WITH daily_sales AS (
    SELECT DATE(order_date) AS sale_date, SUM(unit_price * quantity) AS daily_revenue
    FROM orders
    WHERE order_date >= DATE('now', '-7 days')
    GROUP BY sale_date
)
SELECT ROUND(AVG(daily_revenue), 2) AS avg_revenue_past_7_days
FROM daily_sales;

--Q3.1
------ The reason why it is taking so long may be that it is running over loads of data with a where clause that has no index values to consider that may ease the processing of the 
------ information that it needs to review

--Q3.2
------ In the first instance, PKs have already been created at the beginig of the file, what may lead to improving the processing time of the data. However, composite indexes could 
------ be set for the where statement value that is going to be used to improve the efficiency of the code (i.e. order_date x customer_id within orders)

--Q3.3
CREATE INDEX compidx_orders_date_customer 
ON orders (order_date, customer_id);

SELECT c.customer_id, c.customer_name, SUM(o.quantity * o.unit_price) AS total_revenue
FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_date >= '2025-01-01' 
GROUP BY c.customer_id, c.customer_name;

--Q4.1
CREATE TABLE IF NOT EXISTS shipment_tracking(
    shipment_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    customer_id INT,
    order_date DATE,
    shipment_placement_date DATE,
    estimated_arrival_date DATE,
    status VARCHAR(10),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

---- composed index suggestion - probably delayed orders will be searched for to identigy potential bottlenecks, thus, indexing status and estimated_arrival_date would be of interest.

CREATE INDEX idx_shipments_status_arrival 
ON shipment_tracking (status, estimated_arrival_date);

--Q4.2
CREATE TABLE IF NOT EXISTS product_inventory(
    week_start_date DATE, --Always store a monday (e.g. 2026-10-19)
    product_id INT,
    purchased_per_week INT,
    sold_per_week INT,
    PRIMARY KEY (week_start_date, product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

---- simple index suggestion - considering that it will always be used to review by individual product_id, the index shall be set to such value.

--Q4.3
CREATE TABLE IF NOT EXISTS support_tickets(
    ticket_id INT PRIMARY KEY,
    event_id INT,
    assigned_employee_id INT, -- This would be probably a FK if we had an employee table already created, which shall be 
    status VARCHAR(10),
    rating INT
);

