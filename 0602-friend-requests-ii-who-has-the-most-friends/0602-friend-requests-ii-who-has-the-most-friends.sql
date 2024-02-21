# Write your MySQL query statement below
SELECT t.id, SUM(num) as num
FROM
(
    SELECT accepter_id AS id, COUNT(accepter_id) as num
    FROM RequestAccepted
    GROUP BY accepter_id
    UNION ALL
    SELECT requester_id, COUNT(requester_id)
    FROM RequestAccepted
    GROUP BY requester_id
) t
GROUP BY t.id
ORDER BY num DESC
LIMIT 1