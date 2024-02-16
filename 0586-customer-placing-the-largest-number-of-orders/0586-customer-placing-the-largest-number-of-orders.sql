# Write your MySQL query statement below

SELECT customer_number
FROM (SELECT COUNT(*) AS amount, customer_number
FROM Orders
GROUP BY customer_number) AS combined_orders
ORDER BY amount DESC
LIMIT 1