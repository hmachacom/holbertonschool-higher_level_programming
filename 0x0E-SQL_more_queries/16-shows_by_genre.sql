-- 2 conment
SELECT tv.title, genero.name FROM tv_shows AS tv 
LEFT JOIN tv_show_genres AS uni ON tv.id = uni.show_id 
LEFT JOIN tv_genres AS genero ON genero.id = uni.genre_id ORDER BY tv.title, genero.name ASC;
