//var latLng;
var haveLocation=true; //this will become true after the first time latLng is called.
//I can export only the public methods in geocode, while still keeping the lat and lng and other internals privately within the enclosure private.
var geocode = {}; // This becomes a class.
var address="";
(function(){
    "use strict";
    var maps = google.maps;
    var latLng=null; //A google maps latLng object.
    function setLatLng(lat,lng){ //Clamps latitudes and longitudes if they are out of range.
        latLng = new maps.LatLng(lat,lng);
        if(!haveLocation) haveLocation=true;
    }
    geocode.setLatLng=setLatLng;
    function convertToAddress (){//Do not call this unles you first call setLatLng. It will otherwise have no affect.
    if(!haveLocation) return;
        var geocoder = new maps.Geocoder();
        var geo=geocoder.geocode({location:latLng}, function(results, status){
            if(status == maps.GeocoderStatus.OK){
                address = results[0].formatted_address;
                $("#address").text(address);
            }
        });
    }
    geocode.convertToAddress = convertToAddress;
    function showAddressModal(){
        convertToAddress();
        $("#addressdialog").dialog("open");
    }
    geocode.showAddressModal = showAddressModal;
    function loadMap(){
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 16,
            center: latLng
        });
    };
    geocode.loadMap = loadMap;
}());


