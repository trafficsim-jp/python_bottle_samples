function startVideo() {
    console.info('入出力デバイスを確認してビデオを開始するよ！');

    Promise.resolve()
        .then(function () {
            return navigator.mediaDevices.enumerateDevices();
        })
        .then(function (mediaDeviceInfoList) {
            console.log('使える入出力デバイスs->', mediaDeviceInfoList);

            var videoDevices = mediaDeviceInfoList.filter(function (deviceInfo) {
                return deviceInfo.kind == 'videoinput';
            });
            if (videoDevices.length < 1) {
                throw new Error('ビデオの入力デバイスがない、、、、、。');
            }

            return navigator.mediaDevices.getUserMedia({
                audio: false,
                video: {
                    deviceId: videoDevices[0].deviceId
                }
            });
        })
        .then(function (mediaStream) {
            console.log('取得したMediaStream->', mediaStream);
            videoStreamInUse = mediaStream; console.log(window.URL.createObjectURL(mediaStream));
            //document.querySelector('video').src = window.URL.createObjectURL(mediaStream);
            // 対応していればこっちの方が良い
            document.querySelector('video').srcObject = mediaStream;


        })
        .catch(function (error) {
            console.error('ビデオの設定に失敗、、、、', error);
        });
}

function stopVideo() {
    console.info('ビデオを止めるよ！');

    videoStreamInUse.getVideoTracks()[0].stop();

    if (videoStreamInUse.active) {
        console.error('停止できなかった、、、', videoStreamInUse);
    } else {
        console.log('停止できたよ！', videoStreamInUse);
    }
}

$(function() {
    let videoElement = document.querySelector('video');
    let canvasElement = document.querySelector('canvas');
    let context = canvasElement.getContext('2d');
	let speed = 1000;
	let start = 0;
	let timerName;

	function startflvideo(){
		let jpegbase64 = canvasElement.toDataURL('image/jpeg');
		context.drawImage(videoElement, 0, 0, videoElement.width, videoElement.height);
	    document.querySelector('img').src = jpegbase64;
		let message = { "picture" : jpegbase64 };

		$.ajax({
			type : "POST",
			url:RESTURIROOT+'/movpost',
			contentType: 'application/json; charset=UTF-8',
			dataType: 'json',
			data: JSON.stringify(message),
			success: () => {
				console.log("success");
			},
			error: ()=>{
				console.log("error");
			}
		});
		return;
	}

    $("button#startflvideo").click(function(){
        timerName = setInterval(startflvideo, speed);
    })

    $("button#stopflvideo").click(function(){
        if (timerName) {
            clearInterval(timerName);
        }
    });
});

/*function snapshot() {
    console.info('スナップショットをとるよ！');

    var videoElement = document.querySelector('video');
    var canvasElement = document.querySelector('canvas');
    var context = canvasElement.getContext('2d');

    context.drawImage(videoElement, 0, 0, videoElement.width, videoElement.height);
    document.querySelector('img').src = canvasElement.toDataURL('image/webp');
}

jQuery(()=>{
	$( 'button#saveCanvas' ) .click(
	    () => {

			const imageType = "image/jpeg";

	    	const canvas = document.getElementById("myCanvas");
	    // base64エンコードされたデータを取得 「data:image/png;base64,iVBORw0k～」
	    	base64 = canvas.toDataURL(imageType);
			console.log(base64);

			let message = { "picture" : base64 };
			console.log(message);

			$.ajax({
				type : "POST",
				url:RESTURIROOT+'/picpost',
				contentType: 'application/json; charset=UTF-8',
				dataType: 'json',
				data: JSON.stringify(message),
				success: () => {
					console.log("success");
				},
				error: ()=>{
					console.log("error");
				}
			});
			return;
		});
	});
*/
