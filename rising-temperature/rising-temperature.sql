# Write your MySQL query statement below
SELECT id
FROM Weather AS W
WHERE temperature > 
    (
        SELECT temperature
        FROM Weather
        WHERE Weather.recordDate = SUBDATE(W.recordDate, 1)
    )