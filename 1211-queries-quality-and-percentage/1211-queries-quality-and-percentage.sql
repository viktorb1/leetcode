# Write your MySQL query statement below
SELECT 
    q1.query_name,
    ROUND(AVG(q1.rating/q1.position),2) AS quality,
    ROUND((SELECT COUNT(*) FROM Queries q2 WHERE q2.rating < 3 AND q1.query_name = q2.query_name)/COUNT(*)*100, 2) AS poor_query_percentage
FROM Queries q1
WHERE q1.query_name is NOT NULL
GROUP BY query_name