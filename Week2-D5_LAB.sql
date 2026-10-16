
-- 1

CREATE TABLE orders_perf(
    order_id INT NOT NULL,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    city VARCHAR(10) NOT NULL,
    amount_gbp DECIMAL(10,2) NOT NULL,
    status VARCHAR NOT NULL
);

INSERT INTO orders_perf VALUES
(1, 101, 2026-08-01, "London", 45.50, "complete"),
(2, 102, 2026-08-01, "Manchester", 18.00, "cancelled"),
(3, 101, 2026-08-02, "London", 62.25, "complete"),
(4, 103, 2026-08-02, "Leeds", 30.00, "complete"),
(5, 104, 2026-08-03, "Bristol", 55.50, "complete"),
(6, 102, 2026-08-03, "Manchester", 12.00, "pending"),
(7, 101, 2026-08-04, "London", 80.00, "complete"),
(8, 105, 2026-08-04, "Leeds", 20.00, "complete"),
(9, 106, 2026-08-05, "Bristol", 100.00, "complete"),
(10, 102, 2026-08-05, "Manchester", 40.00, "complete");

--2

EXPLAIN
SELECT
    order_id,
    order_date,
    amount_gbp
FROM orders_perf
WHERE customer_id = 101;

-- 3

CREATE INDEX idx_orders_customer ON orders_perf(customer_id);

EXPLAIN
SELECT
    order_id,
    order_date,
    amount_gbp
FROM orders_perf
WHERE customer_id = 101;

-- 4 B

-- 5

---- QA
SELECT *
FROM orders_perf
WHERE status = 'complete';

---- QB
SELECT
    order_id,
    order_date,
    amount_gbp
FROM orders_perf
WHERE status = 'complete';

------Select all makes the process of retrieving data more demanding for the processor, thats why B makes more sense if its all the info u need

-- 6

SELECT order_id FROM orders_perf
WHERE status = "complete" AND order_date >= 2026-08-03 AND amount_gbp >= 40;

-- 7
CREATE TABLE customers_perf(
    customer_id INT NOT NULL,
    customer_name VARCHAR(10) NOT NULL,
    city VARCHAR(10) NOT NULL
);

INSERT INTO customers_perf VALUES
(101, "Amelia Clarke", "London"),
(102, "Oliver Bennett", "Manchester"),
(103, "Aisha Khan", "Leeds"),
(104, "Harry Thompson", "Bristol"),
(105, "Emily Wilson", "Leeds"),
(106, "Noah Davies", "Bristol");

SELECT o.order_id, c.customer_id, o.amount_gbp, o.status
FROM orders_perf AS o
JOIN customers_perf AS c ON o.customer_id = c.customer_id;

-- 8 C

-- 9  considering that most reports are filtered by date, we shall use order_date as first entry and order by it so it is more readable

-- 10

orders
    order_date = x
        insert data
    order_date = x
        insert data
    etc.

-- 11 excessive file-management - design b due to having more files

-- 12 A

-- 13

            TextorBinary        RoworColumn         CommonStrength
CSV         Text                Row                 Readable
PARQUET     Binary              Column              low storage requiring files
AVRO        Binary              Row                 less storage than standard but less processing required to decompress
ORC         Binary              ?                   ?

-- 14
----A CSV
----B Any can (?)
----C PARQUET
----D PARQIET

-- 15

Text based storage, it is indeed human readable, and its main limitation is the increased storage that it requires

-- 16 D

-- 17

EXPLAIN SELECT order_id, order_date, amount_gbp FROM orders_perf
WHERE customer_id = 101;

CREATE INDEX idx_order_date ON orders_perf(order_date);

EXPLAIN SELECT order_id, order_date, amount_gbp FROM orders_perf
WHERE customer_id = 101;

-- 18

if the select command is all we have it does not need to make the table automatic

-- 19

-- 20