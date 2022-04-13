document.querySelector('DIV#red_header').onclick = () => {
	document.querySelector('header').style.setProperty('color', '#FF0000');

	/* $('header').css('color', '#FF0000'); */

}

/* Diferentes formas de hacer la misma accion
 */
/* 
$clickHeader.onclick = () => {
	document.querySelector('header').style.setProperty('color', '#FF0000');
} */
/* 
$('DIV#red_header').click(() => {
	$('header').css('color', '#FF0000');
	document.querySelector('header').style.setProperty('color', '#FF0000');
}); */