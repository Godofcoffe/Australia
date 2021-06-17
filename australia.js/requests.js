const URL_TO_FETCH = 'https://www.facebook.com/daniely.siqueira.3';
fetch(URL_TO_FETCH, {
  method: 'get' // opcional
})
.then(function(response) {
  response.text()
  .then(function(result) {
    alert(result);
  })
})
.catch(function(err) { 
  alert(err);
});