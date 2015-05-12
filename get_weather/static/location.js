$(document).ready(function(){
    console.log("we are perfect from $.ready");
    if (navigator.geolocation) {
        console.log("location available");
        navigator.geolocation.getCurrentPosition(function(position){
            console.log("in anonimous function of position, ", position);
            var csrftoken = $.cookie('csrftoken');
            console.log(csrftoken);
        function csrfSafeMethod(method) {
            console.log("csrfSafeMethod");
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                console.log("in setup method");
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    console.log("in crsfsafemethod");
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
                console.log("exiting this function!!!!!!");
            }
        });
        console.log("about to make a post request!!!!");
        $.post("forecast",
        {
            lat : position.coords.latitude,
            lng : position.coords.longitude,
            page: page
        },
        function(data, status){
            console.log("I got a reply from the page!");
            //document.write(data);
            console.log("I wrote the data to the page.");
            console.log("btw, the status of the request is ", status)
            //alert(data+"\n\n"+status);
        });
        
        });
    } 
    else
    {
        console.log("well, I guess no location?");
        alert("I am sorry, but I can't seem to get your location. This page requires your location to work.");
    }
    console.log("bye");
});
