# Write your MySQL query statement below

SELECT name as 'Employee' 
FROM Employee AS a
WHERE salary > (SELECT salary FROM Employee WHERE Employee.Id = a.managerId AND a.salary > Employee.salary)