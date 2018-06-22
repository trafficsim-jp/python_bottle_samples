const getfruits = () => {
	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/fruits',
		dataType: 'json',
		success: (res) => {
			let fruitsbox = $("p#fruitsbox");
			console.log(res);
			fruitsbox.text("get fruits: <"+res.fruits+">");
		},
		error: (req,err) => {
		},
		complete: () => {
		}
	});
	return;
};

jQuery(()=>{
	console.log("test");
	console.log(RESTURIROOT);
	$("button#reget").click(()=>{
		getfruits();
	});
	getfruits();
});
