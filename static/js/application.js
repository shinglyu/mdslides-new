window.addEventListener('load', function(){
  //var interval = 1000; // ms
  var loaded = Date.now() / 1000;
  var interval = 2000; // ms
  window.setInterval(function(){
    fetch('/needrefresh/').then(function(resp){
      if (resp.ok){
        return resp.json()
      }
    })
    .then(function(jsonresp){
      console.log(jsonresp['timestamp'] + " > " + loaded + " ?")
      if (jsonresp['timestamp'] > loaded) {
         window.location.replace('http://' + document.domain + ':' + location.port + '/#' + jsonresp['page']);
         window.location.reload(true);
      }
    })
  }, interval);
})

