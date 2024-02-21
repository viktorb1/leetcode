# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance i1
WHERE i1.tiv_2015 IN (SELECT DISTINCT i2.tiv_2015 FROM Insurance i2 WHERE i2.pid != i1.pid)
AND (i1.lat, i1.lon) NOT IN (SELECT DISTINCT i2.lat, i2.lon FROM Insurance i2 WHERE i2.pid != i1.pid)