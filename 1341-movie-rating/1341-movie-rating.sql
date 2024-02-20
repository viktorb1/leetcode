(SELECT Users.name AS results
FROM MovieRating
LEFT JOIN Users ON Users.user_id = MovieRating.user_id
GROUP BY MovieRating.user_id
ORDER BY COUNT(MovieRating.user_id) DESC, Users.name
LIMIT 1)

UNION ALL

(
SELECT Movies.title
FROM MovieRating
LEFT JOIN Movies ON Movies.movie_id = MovieRating.movie_id
WHERE MovieRating.created_at LIKE '2020-02%'
GROUP BY Movies.movie_id
ORDER BY AVG(rating) DESC, Movies.title
LIMIT 1
)