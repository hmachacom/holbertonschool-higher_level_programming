const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, (date) => {
    $('#character').text(date.name);
});