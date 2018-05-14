var localMediaStream = null;
var localScriptProcessor = null;
var bufferSize = 4096;
var audioData = []; // 録音データ
var audioContext =  new AudioContext();

var onAudioProcess = function(e) {
	var input = e.inputBuffer.getChannelData(0);
	var bufferData = new Float32Array(bufferSize);
	for (var i = 0; i < bufferSize; i++) {
		bufferData[i] = input[i];
	}
	audioData.push(bufferData);
};

var startRecorder = function() {
	navigator.getUserMedia(
		{ audio: true },
		function(stream) {
			localMediaStream = stream;
			var scriptProcessor = audioContext.createScriptProcessor(bufferSize, 1, 1);
			localScriptProcessor = scriptProcessor;
			var mediastreamsource = audioContext.createMediaStreamSource(stream);
			mediastreamsource.connect(scriptProcessor);
			scriptProcessor.onaudioprocess = onAudioProcess;
			scriptProcessor.connect(audioContext.destination);
		},
		function(e) {
			console.log(e);
		}
	);
};
//WAVファイルの生成
var exportWAV = function() {
	var encodeWAV = function(samples, sampleRate) {
		var buffer = new ArrayBuffer(44 + samples.length * 2);
		var view = new DataView(buffer);

		var writeString = function(view, offset, string) {
			for (var i = 0; i < string.length; i++){
				view.setUint8(offset + i, string.charCodeAt(i));
			}
		};

		var floatTo16BitPCM = function(output, offset, input) {
			for (var i = 0; i < input.length; i++, offset += 2){
				var s = Math.max(-1, Math.min(1, input[i]));
				output.setInt16(offset, s < 0 ? s * 0x8000 : s * 0x7FFF, true);
			}
		};

		writeString(view, 0, 'RIFF');  // RIFFヘッダ
		view.setUint32(4, 32 + samples.length * 2, true); // これ以降のファイルサイズ
		writeString(view, 8, 'WAVE'); // WAVEヘッダ
		writeString(view, 12, 'fmt '); // fmtチャンク
		view.setUint32(16, 16, true); // fmtチャンクのバイト数
		view.setUint16(20, 1, true); // フォーマットID
		view.setUint16(22, 1, true); // チャンネル数
		view.setUint32(24, sampleRate, true); // サンプリングレート
		view.setUint32(28, sampleRate * 2, true); // データ速度
		view.setUint16(32, 2, true); // ブロックサイズ
		view.setUint16(34, 16, true); // サンプルあたりのビット数
		writeString(view, 36, 'data'); // dataチャンク
		view.setUint32(40, samples.length * 2, true); // 波形データのバイト数
		floatTo16BitPCM(view, 44, samples); // 波形データ

		return view;
	};

	var mergeBuffers = function(audioData) {
		var sampleLength = 0;
		for (var i = 0; i < audioData.length; i++) {
			sampleLength += audioData[i].length;
		}
		var samples = new Float32Array(sampleLength);
		var sampleIdx = 0;
		for (var i = 0; i < audioData.length; i++) {
			for (var j = 0; j < audioData[i].length; j++) {
				samples[sampleIdx] = audioData[i][j];
				sampleIdx++;
			}
		}
		return samples;
	};

	var dataview = encodeWAV(mergeBuffers(audioData), audioContext.sampleRate);
	var audioBlob = new Blob([dataview], { type: 'audio/wav' });

	// バイナリ化した画像をPOSTで送る関数
	var sendWAVBinary = function(blob) {
		var formData = new FormData();
		formData.append('upload', blob);

		$.ajax({
			type: 'POST',
			url:RESTURIROOT+'/postwav',
			data: formData,
			contentType: false,
			processData: false,
			success:function(date, dataType){
				//console.log("succcess");
				//console.log(data);
				window.alert("uploadに成功しました。");
			},
			error: function(XMLHttpRequest, textStatus, errorThrown){
				//console.log("error");
			}
		});
	};

	sendWAVBinary(audioBlob);
	setTimeout("location.reload()", 3000);

/*	var myURL = window.URL || window.webkitURL;
	a = document.createElement("a");
	a.href = myURL.createObjectURL(audioBlob);
	a.target = "_blank";
    a.download = "record.wav";
    event = document.createEvent("MouseEvents");
    event.initEvent("click", false, true);
    a.dispatchEvent(event);
*/

};
