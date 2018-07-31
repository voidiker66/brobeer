function returnHTMLfromString(str, divToAttach) {
	divToAttach.innerHTML = $.parseHTML( str );
}


returnHTMLfromString($('#summary').innerHTML, $('#summary'))