# Write your MySQL query statement below
SELECT s1.product_id, s1.year as "first_year", s2.quantity, s2.price
FROM (SELECT product_id, MIN(year) as year
    FROM Sales
    GROUP BY product_id) s1
LEFT JOIN Sales s2 ON s1.product_id = s2.product_id AND s1.year = s2.year
