-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT gn.name FROM tv_genres AS gn 
LEFT JOIN tv_show_genres AS tv_s ON gn.id = tv_s.genre_id 
LEFT JOIN tv_shows AS tvt_s ON tv_s.show_id = tvt_s.id WHERE tvt_s.title = 'Dexter' GROUP BY name ORDER BY name ASC;
