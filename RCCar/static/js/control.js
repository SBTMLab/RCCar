


/* 주요 키코드
up: 38
down: 40
left: 37
right: 39
*/


var keys = {};

$(document).keydown(function (e) {
    keys[e.which] = true;
});

$(document).keyup(function (e) {
    delete keys[e.which];
});




timer = setInterval(function () {
	keysend();
}, 300);


function keysend() {

	var ajaxdata = new Object();
	ajaxdata.key = keys;


	$.ajax({      
        type:"POST",  
        contentType: "application/json; charset=utf-8",
        url:'/control',      
        data: JSON.stringify(keys),      
        success:function(args){   
        }  
    });  

}