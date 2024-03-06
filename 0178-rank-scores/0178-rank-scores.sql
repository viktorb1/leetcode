SELECT score, 
       (SELECT COUNT(DISTINCT score) 
        FROM Scores s2 
        WHERE s2.score >= s1.score) AS 'rank'
FROM Scores s1
ORDER BY score DESC;
