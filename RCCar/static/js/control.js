


/* 주요 키코드
up: 38
down: 40
left: 37
right: 39
*/


$(document).keydown(function(rs){

	keysend(rs);
});




function keysend(rs) {

	var ajaxdata = new Object();
	ajaxdata.key = rs.which;


	$.ajax({      
        type:"GET",  
        url:'/control',      
        data: ajaxdata,      
        success:function(args){   
            console.log("Success");   
        }  
    });  

}