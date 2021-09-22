$.get('https://fourtonfish.com/hellosalut/?lang=fr', (info) => {
  $('#hello').text(info.hello);
});
