window.onload = () => {
	const $list = document.querySelector('.my_list');
	document.querySelector('DIV#add_item').onclick = () => {
	const element = document.createElement('li');
		element.textContent = 'Item';
		document.querySelector('UL.my_list').appendChild(element);
		const $list = document.querySelector('.my_list');

	}
	document.querySelector('DIV#remove_item').onclick = () => {
		const li = $list.children;
		const last = [...li].pop();
		if (last) {
			document.querySelector('.my_list').removeChild(last);
		}
	}

	document.querySelector('DIV#clear_list').onclick = () => {
		const li = $list.children;
		let lastChildren = [...li].pop();
		while (lastChildren) {
			if (lastChildren) {
				document.querySelector('.my_list').removeChild(lastChildren);
			}
			lastChildren = [...li].pop();			
		}
	}
}