
      var map;
      var directionsDisplay = new google.maps.DirectionsRenderer();
      var directionsService = new google.maps.DirectionsService();      
      function initialize() {
      var myLatlng = new google.maps.LatLng(23.6266557, -102.5375006);
      var mapOptions = {
        zoom: 17,
        center: myLatlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      }
      map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

      var marker_image = new google.maps.MarkerImage('img/icono01.png',new google.maps.Size(48,59),new google.maps.Point(0,0),new google.maps.Point(24,59));
      var shape = {
       coord: [47,0,47,1,47,2,47,3,47,4,47,5,47,6,47,7,47,8,47,9,47,10,47,11,47,12,47,13,47,14,47,15,47,16,47,17,47,18,47,19,47,20,47,21,47,22,47,23,47,24,47,25,47,26,47,27,47,28,47,29,47,30,47,31,47,32,47,33,47,34,47,35,47,36,47,37,47,38,47,39,47,40,47,41,47,42,47,43,47,44,47,45,47,46,47,47,47,48,31,49,31,50,30,51,29,52,28,53,27,54,26,55,26,56,25,57,24,58,23,58,22,57,21,56,21,55,20,54,19,53,18,52,17,51,16,50,16,49,0,48,0,47,0,46,0,45,0,44,0,43,0,42,0,41,0,40,0,39,0,38,0,37,0,36,0,35,0,34,0,33,0,32,0,31,0,30,0,29,0,28,0,27,0,26,0,25,0,24,0,23,0,22,0,21,0,20,0,19,0,18,0,17,0,16,0,15,0,14,0,13,0,12,0,11,0,10,0,9,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0,0,47,0],
       type: 'poly'
     };

   var marker = new google.maps.Marker({
       draggable: true,
       raiseOnDrag: false,
       icon: marker_image,
       shape: shape,
       map: map,
       position: myLatlng
     });

     var dudeMarker = new google.maps.Marker({
      draggable: true,
      raiseOnDrag: false,
      map: map,
    });

    var placeSearch = document.getElementById('geocomplete');
    var defaultBounds = new google.maps.LatLngBounds(
      new google.maps.LatLng(19.4269077, -99.1768632),
      new google.maps.LatLng(19.5070686-99.0273842)
    );

     var optionsAutocomplete = {
          bounds: defaultBounds,
          componentRestrictions: {country: 'mx'},
          types: ['geocode']
      };

    autocomplete = new google.maps.places.Autocomplete(placeSearch, optionsAutocomplete);

    google.maps.event.addListener(autocomplete, 'place_changed', function() {
        
        var place = autocomplete.getPlace();
            if (!place.geometry) {
                  alert('El lugar no fue encontrado');
                return;
            }
            if (place.geometry.viewport) {
                map.fitBounds(place.geometry.viewport);
            } else {
                map.setCenter(place.geometry.location);
                map.setZoom(17);
            }
                dudeMarker.setPosition(place.geometry.location);

                  directionsDisplay.setMap(map);
                  var request = {
                    origin: myLatlng,
                    destination: place.geometry.location,
                    travelMode: google.maps.DirectionsTravelMode.DRIVING
                  };
                  directionsService.route(request, function(response, status) {
                    if (status == google.maps.DirectionsStatus.OK) {
                      directionsDisplay.setDirections(response);
                    }
                  });
        });
    }