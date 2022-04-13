const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
    $.each(data.results, function (iterador, pelicula) {
        $('#list_movies').append('<li>' + pelicula.title + '</li>');
    });
});