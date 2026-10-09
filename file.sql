create database file1

create table Employee(
    employee_id integrer primary key 
    name text not NULL
    department text not null
);

-- insert

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  city VARCHAR(50)
);
 
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  amount_gbp DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


--- Exampleeeees:

drop table if exists Products;

CREATE TABLE Products (
  product_id INT PRIMARY KEY,
  sku VARCHAR(50) UNIQUE,
  price DECIMAL(10,2) NOT NULL,
  quantity INT,
  expire_date DATE
);
 
INSERT INTO Products (product_id, sku, price, quantity, expire_date) VALUES
(1, 'SKU-001', 200099999999999.23, 10, '2029-10-02');

INSERT INTO Products (product_id, sku, price, quantity, expire_date) VALUES
(2, 'SKU-002', 32.24, 10, '2029-10-03'),
(3, 'SKU-003', 2.22, 10, '2029-10-04'),
(4, 'SKU-004', 33.63, 12, '2029-10-05'),
(5, 'SKU-005', 67.25, 24, '2029-10-06'),
(6, 'SKU-006', 99.34, 43, '2029-10-07');


SELECT * FROM Products; 

UPDATE Products SET product_id = 333, price = 333.33 WHERE sku = 'SKU-003';

SELECT * FROM Products; 

-- for updating values: UPDATE xx_variable SET table_it_is_in = 'Name of the table' WHERE where_shall_it_be_changed_example_customer_id = x;
-- for deleting values: DELETE FROM table_it_is_in WHERE where_shall_it_be_changed_example_customer_id = x;
-- for creating: INSERT INTO xx_table(vale1, value2,..) VALUES (insert,values,that,neec,to,match,theonesstatedpreviousñ)

DELETE from Products where product_id = 333;
select count(*) as count_products FROm Products where product_id = 333;

drop table if exists Products;

CREATE TABLE l_tal (
  n_id INT PRIMARY KEY,
  name_ VARCHAR(50) UNIQUE,
  age INT
);

CREATE TABLE r_tal (
  n_id INT PRIMARY KEY,
  name_ VARCHAR(50),
  age INT,
  city_ VARCHAR(50)
);

INSERT into l_tal(n_id, name_, age) VALUES
(1, 'Carlos', 55),
(2, 'Maria', 33),
(3, 'Mario', 66);

INSERT into r_tal(n_id, name_, age, city_) VALUES
(1, 'Carlos', 55, 'Madrid'),
(2, 'Mary', 33, 'Cairo'),
(3, 'Mario', 66, 'Berlin'),
(4, 'Miguel', 55, 'San Francisco');

SELECT rt.n_id, rt.name_, rt.age, rt.city_ 
FROM r_tal rt 
JOIN l_tal lt ON rt.n_id = lt.n_id
ORDER BY rt.n_id;

