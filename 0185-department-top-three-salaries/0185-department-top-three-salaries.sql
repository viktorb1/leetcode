# Write your MySQL query statement below
SELECT d.name as Department, e1.name as Employee, salary as Salary
FROM Employee e1
LEFT JOIN Department d ON d.id = e1.departmentId
WHERE e1.salary >= COALESCE(
    (
    SELECT DISTINCT e2.salary
    FROM Employee e2
    WHERE e2.departmentId = e1.departmentId
    ORDER BY e2.salary DESC
    LIMIT 1 OFFSET 2
    )
, 0)
