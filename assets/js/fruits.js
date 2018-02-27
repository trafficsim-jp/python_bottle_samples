// 今どきの関数定義
const getfruits = () => {
	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/fruits',
		dataType: 'json',
		success: (res) => {
			//サーバから返答がもらえた
			let fruitsbox = $("p#fruitsbox");
			console.log(res);
			fruitsbox.text("get fruits: <"+res.fruits+">");
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
	$("button#reget").click(()=>{
		getfruits();
	});
	getfruits();
});
