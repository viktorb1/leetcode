SELECT ROUND(COUNT(a2.player_id) / COUNT(a1.player_id), 2) as fraction
FROM
(SELECT player_id, MIN(event_date) AS min_event_date
FROM Activity
GROUP BY player_id) a1
LEFT JOIN Activity a2 
ON a1.player_id = a2.player_id AND DATEDIFF(a2.event_date, a1.min_event_date) = 1