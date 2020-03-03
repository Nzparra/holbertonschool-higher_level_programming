-- that lists all tv_shows contained in hbtn_0d_tvtv_shows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY 1, 2;
