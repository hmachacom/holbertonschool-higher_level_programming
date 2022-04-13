document.querySelector('DIV#toggle_header').onclick = () => {
	const list = document.querySelector('header').classList
	/* if (list.value === "green") {
		list.remove('green');
		list.add('red');
	}
	else {
		if (list.value === "red") {
		list.remove('red');
		list.add('green');
	}	
	} */
	list.toggle("green");
	list.toggle("red");

}