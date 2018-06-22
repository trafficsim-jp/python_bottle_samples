let dataUrl;
let objFile = document.getElementById("image_select");
objFile.addEventListener("change", function(evt) {
	let file = evt.target.files;
	let reader = new FileReader();
	reader.readAsDataURL(file[0]);
	reader.onload = function(){
		let dataUrl = reader.result;
		document.getElementById("pre_image").innerHTML = "<img id=\"pre_image\"src='" + dataUrl + "'>";
	}
}, false);

jQuery(()=>{
	$('button#object_detection').click(
	    () => {
			const imageType = "image/jpeg";
			let pre_image = $('img#pre_image');
			let base64 = pre_image[0].src;
			let message = { "picture" : base64 };
			console.log(message);

			$.ajax({
				type : "POST",
				url:RESTURIROOT+'/launch_darknet',
				contentType: 'application/json; charset=UTF-8',
				dataType: 'json',
				data: JSON.stringify(message),
				success: () => {
					console.log("success");
				},
				error: ()=>{
					console.log("error");
				}
			}).done(function(res){
				document.getElementById("post_image").innerHTML = "<img id=\"post_image\"src='" + res + "'>";
			})
		}
	);
});

/*
let dataUrl;
let objFile = document.getElementById("image_select");
objFile.addEventListener("change", function(evt) {
	let file = evt.target.files;
	let reader = new FileReader();
	reader.readAsDataURL(file[0]);
	reader.onload = function() {
		console.log("onloadされました")
		let dataUrl = reader.result;
		if(false){
			document.getElementById("pre_image").innerHTML = "<img src='" + dataUrl + "'>";
		}
		else {
			let canvas = document.getElementById("pre_image");
			let ctx2d = canvas.getContext('2d')
			let preimg = new Image;
			preimg.onload = function() {
				ctx2d.drawImage(this,
								0, 0, this.width, this.height,
								0, 0, canvas.width, canvas.height
								);
			}
			preimg.src = dataUrl;
		}
    };
}, false);
*/
