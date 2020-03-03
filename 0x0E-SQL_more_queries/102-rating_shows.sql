-- that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT title, SUM(rate) as rating
FROM tv_shows
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY 1
ORDER BY 2 DESC;