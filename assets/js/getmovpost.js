const getfruits = () => {
	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/getmovpost',
		dataType: 'json',
		success: (res) => {
			//サーバから返答がもらえた
			let fruitsbox = $("p#fruitsbox");
			console.log(res);
			$("p#fruitsbox").text("get fruits: <"+res.fruits+">");
		},
		error: (req,err) => {
			//サーバから返答が何らかの形で失敗した.
		},
		complete: () => {
			//成功/失敗に拘わらず通信が終われば此処に来る.
		}
	});
    return;
};
