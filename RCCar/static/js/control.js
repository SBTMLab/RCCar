


/* 주요 키코드
up: 38
down: 40
left: 37
right: 39
*/


var keys = {};

$(document).keydown(function (e) {
    keys[e.which] = true;
    ajaxkeysend();

});

$(document).keyup(function (e) {
    delete keys[e.which];
    ajaxkeysend();
});



function ajaxkeysend() {

	var ajaxdata = new Object();
	ajaxdata.key = keys;

	$.ajax({      
        type:"POST",  
        dataType : 'json',
        contentType: "application/json; charset=utf-8",
        url:'/control',      
        data: JSON.stringify(keys),      
        success:function(args){   
        }  
    });  

}
