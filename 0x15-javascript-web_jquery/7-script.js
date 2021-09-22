$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (info) {
  $('DIV#character').text(info.name);
});
