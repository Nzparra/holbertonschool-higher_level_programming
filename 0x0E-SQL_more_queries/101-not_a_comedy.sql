--  uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id =  tv_shows.id
LEFT JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title NOT IN (
SELECT DISTINCT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show_genres.show_id =  tv_shows.id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY 1);
