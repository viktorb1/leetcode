# Write your MySQL query statement below
SELECT *
FROM
(
    SELECT s1.id, COALESCE(s2.student, s1.student) AS student
    FROM Seat s1
    LEFT JOIN Seat s2 ON s2.id = s1.id + 1
    WHERE s1.id % 2 = 1
    
    UNION
    
    SELECT s1.id, s2.student
    FROM Seat s1
    LEFT JOIN Seat s2 ON s2.id = s1.id - 1
    WHERE s2.id % 2 = 1
    
) t
ORDER BY id ASC