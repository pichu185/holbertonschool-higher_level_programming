$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (json_info) {
  $('DIV#character').text(json_info.name);
});
