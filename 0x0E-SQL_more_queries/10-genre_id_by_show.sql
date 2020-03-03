-- that lists all shows contained in hbtn_0d_tvshows
SELECT shows.title, genre.genre_id FROM tv_shows as shows
JOIN tv_show_genres as genre ON shows.id = genre.show_id
ORDER BY shows.title, genre.genre_id ASC;
