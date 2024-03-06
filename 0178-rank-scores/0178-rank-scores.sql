SELECT score, 
       (SELECT COUNT(score) 
        FROM (SELECT DISTINCT score FROM Scores) AS s2
        WHERE s2.score >= s1.score) AS 'rank'
FROM Scores s1
ORDER BY score DESC;
