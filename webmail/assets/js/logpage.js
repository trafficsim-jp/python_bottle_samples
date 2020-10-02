
function init_page(){
	$.ajax({
		type: 'GET',
		url: RESTURIROOT+'/sendmail/log',
		dataType: 'json',
		success:(res) => {
			$("textarea#logdisp").val(res.log);
		},
		error: (req,status,err) => {
			alert("log could not be getten.");
		},
		complete: ()=>{
		}
	});
}

jQuery(()=>{
	console.log("load logpage.js");
	console.log(RESTURIROOT);

	init_page();
});
