$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (json_info) {
  $('UL#list_movies').append(...json_info.results.map(movie => `<li>${movie.title}</li>`));
});
