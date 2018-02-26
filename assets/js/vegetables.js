// 今どきの関数定義
const getvegetables = () => {
	$.ajax({
		type: 'GET',
		url:RESTURIROOT+'/vegetables',
		dataType: 'json',
		success: (res) => {
			//サーバから返答がもらえた
			let vegetablesbox = $("p#vegetablesbox");
			console.log(res);
			$("p#vegetablesbox").text("get vegetables: <"+res.vegetables+">");
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
		getvegetables();
	});
	getvegetables();
});
