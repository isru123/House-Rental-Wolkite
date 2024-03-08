function trackLocation() {
    var location = document.getElementById("location").value;
    var geocoder = new google.maps.Geocoder();
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: {lat: -34.397, lng: 150.644} // Default center (Sydney, Australia)
    });

    geocoder.geocode({ 'address': location }, function(results, status) {
        if (status === 'OK') {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}
