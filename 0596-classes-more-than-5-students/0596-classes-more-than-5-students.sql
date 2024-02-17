# Write your MySQL query statement below
SELECT class
FROM (SELECT class, COUNT(*) as count
FROM Courses
GROUP BY class) c1
WHERE c1.count >= 5