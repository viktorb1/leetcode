# Write your MySQL query statement below
SELECT customer_id, COUNT(*) as count_no_trans
FROM Visits
LEFT JOIN (SELECT * FROM Transactions WHERE amount IS NOT NULL) as Transactions_ on Visits.visit_id = Transactions_.visit_id
WHERE amount IS NULL
GROUP BY customer_id