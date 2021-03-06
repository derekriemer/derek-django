/*This file Copyright (C) Derek Riemer, 2016
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
    along with my personal website.  If not, see <http://www.gnu.org/licenses/>.
*/
assending= [true, 0]; // be sure this is pointing at the right column. Currently it points at hourly.
function makeTable(col){
    if(assending[1] != col){        assending = (col == 0 ? [true, col] : [false, col]);
    }
    else
    {
        assending[0] = ! assending[0];
    }
    var new_table= table.sort(function(a,b){
        if(assending[0]){ // Ascending[0] is the actual whether we are ascending or decending mode. 
            switch(assending[1]){
                case 0: // col 0 has a relative hour index, and the ID to produce..
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
    var new_string = "<tr><th> <h2><a href =\"javascript:void(0)\" onclick=\"makeTable(0)\">Hour:</a></h2></th><th> <a href =\"javascript:void(0)\" onclick=\"makeTable(1)\">Temperature:</a></th><th> <a href =\"javascript:void(0)\" onclick=\"makeTable(2)\">Chance of precip:</a></th></tr>";
    for(var e = 0; e < new_table.length; e++){
        i = new_table[e];
        new_string+="<tr>";
        new_string+="<th><h2>"+i[0][1]+"</h2></th>"; //i[0] hourly, [1] is the id to put here.]        new_string += "<td>"+i[1]+"&#176;"+tempUnits+"</td>"        new_string += "<td>"+i[2]+"%</td></tr>";
    }
    $("#dynamic_table_hourly_forecast").html(new_string)
    fillTable();
    
    new_string="Table sorted by ";
    new_string+=assending[0] ? "assending " : "decending ";
    new_string += ["hour","temperature","precipitation"][assending[1]];
    $("#statusbar").html(new_string); //Announce the update to screen reader users who visually can't see the red cells appear.
}