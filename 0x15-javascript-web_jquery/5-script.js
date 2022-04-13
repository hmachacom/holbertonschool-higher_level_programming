document.querySelector('DIV#add_item').onclick = () => {
	const element = document.createElement('li');
	element.textContent = 'Item'
	document.querySelector('UL.my_list').appendChild(element)
}