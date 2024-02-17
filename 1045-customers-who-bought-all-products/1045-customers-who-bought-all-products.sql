# Write your MySQL query statement below
SELECT c1.customer_id
FROM
(SELECT *
FROM Customer
GROUP BY customer_id, product_key) c1
GROUP BY customer_id
HAVING COUNT(*) = (SELECT COUNT(*) FROM Product)