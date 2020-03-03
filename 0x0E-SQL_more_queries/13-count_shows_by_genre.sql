-- that lists all shows contained in hbtn_0d_tvshows
SELECT shows.name AS 'genre', COUNT(*) AS number_of_shows
FROM tv_genres AS shows
INNER JOIN tv_show_genres AS genre
ON shows.id = genre.genre_id
GROUP BY 1
ORDER BY 2 DESC;
