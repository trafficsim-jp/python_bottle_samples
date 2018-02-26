const posttext = (text) => {
	let message = { posttext : text };
/*	let message2 = { posttext : 200 };
	console.log(text);
	console.log(JSON.stringify(text));
	console.log(message);
	console.log(JSON.stringify(message));
	console.log(message2);
	console.log(JSON.stringify(message));*/
	$.ajax({
		type : "POST",
		url:RESTURIROOT+'/posttest',
		contentType: 'application/json; charset=UTF-8',
		dataType: 'json',
		data: JSON.stringify(text),
		success: () => {
			console.log("success");
		},
		error: ()=>{
			console.log("error");
		}
	});
	return;
}

jQuery(()=>{
	console.log("test");
	console.log(RESTURIROOT);
	$("input#button").click(()=>{
		console.log("click");

		posttext($("input#posttext").val())
	});
});
