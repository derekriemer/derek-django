$(document).ready(function(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position){
            csrf_token=$("input[name='csrfmiddlewaretoken']").attr("value");
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
