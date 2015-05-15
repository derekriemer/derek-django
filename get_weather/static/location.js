$(document).ready(function(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position){
        // using jQuery
        var csrf_token;
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
        csrf        _token = getCookie('csrftoken');
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
        $.post("forecast",
        {
            lat : position.coords.latitude,
            lng : position.coords.longitude,
            page: page
        },
        function(data, status){
            document.write(data);
            //alert(data+"\n\n"+status);
        });
        
        });
    } 
    else
    {
        console.log("well, I guess no location?");
        alert("I am sorry, but I can't seem to get your location. This page requires your location to work.");
    }
});
