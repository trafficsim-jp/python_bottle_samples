
function submit_server_setting(){
	console.log("submit_server_setting");

	let submit_promise =
		new Promise((resolve) => {
			// kickだけおこなう.
			resolve();
		});

	submit_promise
		.then(() => {
			console.log("check smpt_server");
			let smtp_server = $("input#smtp_server").val();
			if(smtp_server == "") {
				throw new Error('invalid smpt server address');
			}
			return smtp_server;
		})
		.then((smtp_server) => {
			console.log("post smtp_server:"+smtp_server);
			// jQueryのDeferredで通信結果待ちを行います.
			var d = new $.Deferred();
			$.ajax({
				type: "POST",
				contentType: "application/json",
				dataType: "json",
				url: RESTURIROOT+'/sendmail/smtp_server',
				data: JSON.stringify({ smtp_server : smtp_server }),
				success:(res) => {
					d.resolve();
				},
				error: (req,status,err) => {
					d.reject(Error('failed to post smtp server address'));
				},
				complete: () => {
				}
			});
			return d.promise();
		})
		.then(
			() => {
				console.log("check smpt_port");
				let smtp_server_port = Number($("input#smtp_port").val());
				if (typeof smtp_server_port === "undefined") {
					throw new Error('invalid smtp server port');
				}
				if (smtp_server_port == 0){
					throw new Error('invalid smtp server port');
				}
				return smtp_server_port;
			},
			(e)=>{
				//前回のthenで失敗したときにここに来ます.
				throw e;
			})
		.then((smtp_server_port)=>{
			var d = new $.Deferred();
			$.ajax({
				type: 'POST',
				contentType: "application/json",
				dataType: "json",
				url: RESTURIROOT+'/sendmail/smtp_server_port',
				data: JSON.stringify({smtp_server_port : smtp_server_port}),
				success:(res) => {
					d.resolve();
				},
				error: (req,status,err) => {
					d.reject(Error('failed to post smtp server port'));
				},
				complete: () => {
				}
			});
			return d.promise();
		})
		.then(
			() => {
				let username = $("input#inputusername").val();
				if (username == ""){
					throw new Error('invalid username');
				}
				return username;
			},
			(e) => {
				//前回のthenで失敗したときにここに来ます.
				throw e;
			}
		)
		.then(
			(username) => {
				console.log("POST username:"+username);
				var d = new $.Deferred();
				$.ajax({
					type: 'POST',
					contentType: 'application/json',
					dataType: 'json',
					url: RESTURIROOT+'/sendmail/username',
					data: JSON.stringify({ username : username }),
					success:(res) => {
						d.resolve();
					},
					error: (req, status, err) => {
						d.reject(Error('failed to post username'));
					},
					complete: () => {
					}
				});
				return d.promise();
			})
		.then(
			() => {
			},
			(e)=>{
				throw e;
			}
		)
		.catch((e) => {
			console.log(e);
			alert(e);
		})
		.finally(() => {
			//失敗成功に関わらず必ず呼び出されます.
			console.log("finally");
			//設定項目の更新
			init_page();
		});
}

function submit_address_setting(){
	console.log("submit_address_setting");
}

function init_page(){

	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/sendmail/smtp_server',
		dataType: 'json',
		success:(res) => {
			console.log(res);
			$("input#smtp_server").val(res.smtp_server);
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
			console.log("get smtp_server_port");
			console.log(res);
			if(res.smtp_server_port == 0){
				// 設定されていない
				// default値を入れておく
				$("input#smtp_port").val(587);
			}
			else {
				$("input#smtp_port").val(res.smtp_server_port);
			}
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
			if (res.username != "") {
				username_input.val(res.username);
			}
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

	$("button#address_setting").click(()=>{
		submit_address_setting();
	});

	$("button#server_setting").click(()=>{
		submit_server_setting();
	});
});
