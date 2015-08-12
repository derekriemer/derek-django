const CUTE_PUPPY="/static/cute_puppy.jpg"; //part of easterEgg_cute_puppy.

function friendlyHourNames(hour){
    varmarker="";
    if(hour==0){
        return "midnight";
    }
    else if (hour < 12){
        return hour+" A.M.";
    }
    else if(hour==12){
        return "Noon";
    }
    else
    {
        return (hour-12)+" P.M."
    }
}
