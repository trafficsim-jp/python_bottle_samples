// 今どきの関数定義
const currenttext = () => {
	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/currenttext',
		dataType: 'json',
		success: (res) => {
			//サーバから返答がもらえた
			let currenttextbox = $("p#currenttextbox");
			console.log(res);
			$("p#currenttextbox").text("現在 " +res.currenttext+ " がポストされています");
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
	console.log("test");
	console.log(RESTURIROOT);
	$("button#update").click(()=>{
		currenttext();
	});
	currenttext();
});
