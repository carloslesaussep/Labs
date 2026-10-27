SELECT 
    order_id, 
    LOWER(customer) AS customer, 
    LOWER(city) AS city, 
    LOWER(product) AS product, 
    quantity, 
    price, 
    (quantity * price) AS total_amount 
FROM {{ ref('sales_raw') }}