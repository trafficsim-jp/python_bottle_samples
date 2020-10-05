
function init_page() {
	$.ajax({
		type: 'GET',
		url: RESTURIROOT+'/line_notify/access_token',
		dataType: 'json',
		success:(res) => {
			$("input#token").val(res.access_token);
		},
		error:(req, status, err) => {
			if(req.status == 404){
				//設定されていない
			}
			else {
			}
		},
		complete: ()=>{
		}
	});
}

function submit_register(){
	let access_token = $("input#token").val();
	$.ajax({
		type: 'POST',
		contentType: 'application/json',
		dataType: 'json',
		url: RESTURIROOT+'/line_notify/access_token',
		data: JSON.stringify({access_token : access_token}),
		success:(res) => {
			alert("success to register access token");
		},
		error:(req, status, err) => {
			alert("failed to register access token");
		},
		complete:() => {
			init_page();
		}
	});
}


jQuery(()=>{
	console.log("load register page");
	init_page();
	$("button#register").click(() => {
		submit_register();
	});
});
