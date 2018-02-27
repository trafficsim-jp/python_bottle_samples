const currentmov = () => {
	let videoElement = document.querySelector('video');
    let canvasElement = document.querySelector('canvas');
    let context = canvasElement.getContext('2d');
	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/getmovpost',
		dataType: 'json',
		success: (res) => {
			//サーバから返答がもらえた
			let bodies = res.currentmov
			console.log(bodies);
			let body = window.atob(bodies)
			console.log(body);
			context.drawImage(videoElement, 0, 0, videoElement.width, videoElement.height);
			document.querySelector('img').src = body;
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
	setInterval(currentmov, 1000);
});
