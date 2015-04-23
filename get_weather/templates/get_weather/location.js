if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position){
        if (window.XMLHttpRequest)
        {// code for IE7+, Firefox, Chrome, Opera, Safari
            xmlhttp=XMLHttpRequest();
        }
    else
    {// code for IE6, IE5
        alert("We don't really care to support your browser! You are running something old and antiquated and should upgrade to technology that isn't as old as man.");
        return;
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.write(xmlhttp.responseText);
        }
    }
    xmlhttp.open("POST","weather/forecast",true);
    xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    xmlhttp.send("lat="+position.coords.latitude+"&lng="+position.coords.longitude+"&page="+{{page}});
    });
} 

