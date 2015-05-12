$(document).ready(function(){
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position){
            
            var csrftoken = $.cookie('csrftoken');
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        $.post("weather/forecast",
        {
            lat : position.coords.latitude,
            lng : position.coords.longitude,
            page: page
        },
        function(data, status){
            document.write(data);
            alert(data+"\n\n"+status);
            setTimeout(function(){
                document.getElementById("skip").setFocus();
            }, 30);;
        });
        
        });
    } 
    else
    {
        alert("I am sorry, but I can't seem to get your location. This page requires your location to work.");
    }
});
