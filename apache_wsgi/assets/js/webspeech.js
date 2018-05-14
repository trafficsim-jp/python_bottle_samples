let flag_speech = 0;

function vr_function() {
	window.SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
	let recognition = new webkitSpeechRecognition();
    recognition.lang = 'ja';
    recognition.interimResults = true;
    recognition.continuous = true;

    recognition.onsoundstart = function() {
        document.getElementById('status').innerHTML = "認識中";
    };
    recognition.onnomatch = function() {
        document.getElementById('status').innerHTML = "もう一度試してください";
    };
    recognition.onerror = function() {
        document.getElementById('status').innerHTML = "エラー";
        if(flag_speech == 0)
          vr_function();
    };
    recognition.onsoundend = function() {
        document.getElementById('status').innerHTML = "停止中";
          vr_function();
    };

    recognition.onresult = function(event) {
        let results = event.results;
        for (let i = event.resultIndex; i < results.length; i++) {
            if (results[i].isFinal){
                document.getElementById('result_text').innerHTML = results[i][0].transcript;
                vr_function();
            }
            else{
                document.getElementById('result_text').innerHTML = "[途中経過] " + results[i][0].transcript;
                flag_speech = 1;
            }
        }
    };

    flag_speech = 0;
    document.getElementById('status').innerHTML = "start";
    recognition.start();
}

function vrabort_function(){
	document.getElementById('status').innerHTML = "認証停止";
	recognition.stop();
}
