SELECT d.name as Department, e.name as Employee, salary as Salary
FROM Employee e
LEFT JOIN Department d ON e.departmentId = d.id 
WHERE (e.salary, e.departmentId) IN (
    SELECT MAX(salary), departmentId
    FROM Employee
    GROUP BY departmentId
)