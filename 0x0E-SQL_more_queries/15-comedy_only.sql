-- coment
SELECT tv.title FROM tv_shows AS tv 
LEFT JOIN tv_show_genres AS uni ON uni.show_id = tv.id 
LEFT JOIN tv_genres AS genero ON uni.genre_id = genero.id WHERE genero.name = 'Comedy' GROUP BY title ORDER BY title ASC;
