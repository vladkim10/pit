function donate() {
$("#donfr").fadeIn("slow");
}

function x() {
$("#donfr").fadeOut("slow");
}

$(document).ready(function() {
	$('#myCarousel').carousel({
	interval: 10000
	})
    
    $('#myCarousel').on('slid.bs.carousel', function() {
    	//alert("slid");
	});
    
    
});


function showClient() {
$("#clientfr").fadeIn("slow");
}

function closeClient() {
$("#clientfr").fadeOut("slow");
}

function showAdd_pet() {
$("#add_petfr").fadeIn("slow");
}

function closeAdd_pet() {
$("#add_petfr").fadeOut("slow");
}

function showTrans() {
$("#transfr").fadeIn("slow");
}

function closeTrans() {
$("#transfr").fadeOut("slow");
}


