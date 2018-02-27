const currentmov = () => {
	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/getmovpost',
		dataType: 'json',
		success: (res) => {
			//サーバから返答がもらえた
			console.log(res);
			document.querySelector('img').src = res.currentmov;
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

jQuery(()=>{
	setInterval(currentmov(), 1000);
});
