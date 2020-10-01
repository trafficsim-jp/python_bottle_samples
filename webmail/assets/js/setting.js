
function submit_server_setting(){

}

function init_page(){

	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/sendmail/smtp_server',
		dataType: 'json',
		success:(res) => {
		},
		error: (req,status,err) => {
			if(req.status == 404){
				//設定されていない
			}
		},
		complete: () => {
		}
	});

	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/sendmail/smtp_server_port',
		dataType: 'json',
		success:(res) => {
		},
		error: (req,status,err)=> {
			if(req.status == 404){
				// 設定されていない
				// default値を入れておく
				let smtp_server_port_input = $("input#smtp_port");
				smtp_server_port_input.val(587);
			}
		},
		complete: () => {
		}
	});

	$.ajax({
		type: 'GET',
		url: RESTURIROOT+'/sendmail/username',
		dataType: 'json',
		success:(res)=> {
			let username_input = $("input#inputusername");
			if (res.username == "") {
				username_input.val(res.username);
			}
			console.log(res);
		},
		error: (req,status,err) => {
			if(req.status == 404){
				//設定されていない
			}
			else {
			}
		},
		complete: ()  => {
		}
	});

	$.ajax({
		type: 'GET',
		url: RESTURIROOT+'/sendmail/password',
		dataType: 'json',
		success:(res) => {
		},
		error: (req,status,err) => {
			if(req.status == 404){
				//設定されていない
			}
			else {
			}
		},
		complete: ()=>{
		}
	});

	$.ajax({
		type: 'GET',
		url: RESTURIROOT+'/sendmail/from_address',
		dataType: 'json',
		success:(res) => {
		},
		error: (req,status,err) => {
			if(req.status == 404){
				//設定されていない
			}
			else {
			}
		},
		complete: ()=>{
		}
	});

	$.ajax({
		type: 'GET',
		url: RESTURIROOT+'/sendmail/dest_addresses',
		dataType: 'json',
		success:(res) => {
		},
		error: (req,status,err) => {
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

jQuery(()=>{
	console.log("load setting.js");
	console.log(RESTURIROOT);

	init_page();

	$("button#server_setting").click(()=>{
		submit_server_setting();
	});
});
