SELECT c.customer_id, COUNT(o.order_id) AS order_count, COALESCE(SUM(o.unit_price * o.quantity), 0) AS total_sales, COALESCE(AVG(o.unit_price * o.quantity), 0) AS average_order
FROM {{ ref('customers') }} AS c
LEFT JOIN {{ ref('orders') }} AS o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY total_sales DESC