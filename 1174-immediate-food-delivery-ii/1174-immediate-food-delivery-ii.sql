# Write your MySQL query statement below
SELECT ROUND(SUM(IF(d1.order_date = d1.customer_pref_delivery_date, 1, 0))/COUNT(*)*100,2) as immediate_percentage
FROM Delivery d1
WHERE (d1.customer_id, d1.order_date) IN
(SELECT d2.customer_id, MIN(d2.order_date)
FROM Delivery d2
GROUP BY d2.customer_id)