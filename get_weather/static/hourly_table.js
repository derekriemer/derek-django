assending= [true, 0]; // be sure this is pointing at the right column. Currently it points at hourly.
function makeTable(col){
	if(assending[1] != col){
		assending = [false, col];
	}
	else
	{
		assending[0] = ! assending[0];
	}
	var new_table= table.sort(function(a,b){
		if(assending[0]){
			switch(assending[1]){
				case 0:
					return a[0][0]-b[0][0];
				default:
					return a[assending[1]]-b[assending[1]];
			}
		}
		else
		{
			switch(assending[1]){
				case 0:
					return b[0][0]-a[0][0];
				default:
					return b[assending[1]]-a[assending[1]];
			}
		}
	});
	
	var new_string = "<tr>";
	new_string+="<th class='col_1'> <h2><a href =\"javascript:void(0)\" onclick=\"makeTable(0)\">Hour:</a></h2></th>";
	new_string+="<th class='col_2'> <a href =\"javascript:void(0)\" onclick=\"makeTable(1)\">Temperature:</a></th><th class='col_3'> <a href =\"javascript:void(0)\" onclick=\"makeTable(2)\">Chance of precip:</a></th></tr>";
	for(var e = 0; e < new_table.length; e++){
		i = new_table[e];
		new_string+="<tr class='dynamic'>";
		new_string+="<th class='col_1'>"+i[0][1]+"</th><td class='col_2'>"+i[1]+"&#176;F</td><td class='col_3'>"+i[2]+"%</td></tr>";
	}
	$("#dynamic_table_hourly_forecast").html(new_string);
    new_string="Table sorted by ";
	new_string+=assending[0] ? "assending " : "decending ";
	new_string += ["hour","temperature","precipitation"][assending[1]];
	$("#statusbar").html(new_string);
    var colm=col+1;
	$(".col_"+(col+1)).each(function(index, item){
        this.setAttribute("class", "selected");
	});
	
}