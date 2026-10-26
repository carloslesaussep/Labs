SELECT p.product_id, COALESCE(SUM(o.quantity), 0) AS unit_sales, COALESCE(SUM(o.quantity * o.unit_price), 0) AS product_revenue
FROM {{ ref('products') }} AS p
LEFT JOIN {{ ref('orders') }} AS o ON p.product_id = o.product_id
GROUP BY p.product_id
ORDER BY product_revenue DESC









