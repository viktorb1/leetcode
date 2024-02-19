# Write your MySQL query statement below

SELECT product_name, fp.total AS unit
FROM Products
INNER JOIN (
SELECT *, SUM(unit) AS total
FROM orders
WHERE MONTH(order_date) = 2 AND YEAR(order_date) = 2020
GROUP BY product_id
HAVING total >= 100
) AS fp
ON Products.product_id = fp.product_id