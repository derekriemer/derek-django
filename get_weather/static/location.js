var a;
    /*This file Copyright (C) Derek Riemer, 2015
	This file is part of my personal website.

	my personal website is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	The code of my personal website is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with my personal website.  If not, see <http://www.gnu.org/licenses/>.*/
$(document).ready(function(){
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrf_token = getCookie('csrftoken');
    function queryMyApi(lat,lng){
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            }
        });
        a = $.post("forecast",
        {
            lat :lat,
            lng :lng,
            page: page
        },
        function(data, status){
            console.log(status);
            geocode.setLatLng(lat,lng);
            console.log("ok");
            $("#main").html(data);
            $("#skip").focus();
            $("#footer").before('<div class="row"><button onclick="geocode.showAddressModal()"> Show my current address</button></div>');
            //alert(data+"\n\n"+status);
        });
    }
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position){
            queryMyApi( position.coords.latitude,position.coords.longitude)
        },
        function err(){
        alert("Sorry. Error receiving weather data. I can't get your location.")},
        {
            enableHighAccuracy: true, 
            maximumAge        : 30000, 
            timeout           : 30000
        });
    } 
    else
    {
        console.log("well, I guess no location?");
        alert("I am sorry, but I can't seem to get your location. This page requires your location to work.");
    }
});
