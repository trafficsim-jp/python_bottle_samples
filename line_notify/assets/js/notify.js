
function submit_notify() {
	let message = $("textarea#notifymessage").val();

	console.log("submit notify");

	$.ajax({
		type: 'POST',
		contentType: 'application/json',
		dataType: 'json',
		url: RESTURIROOT+'/line_notify/notify',
		data: JSON.stringify({message : message}),
		success:(res) => {
			alert("success to notify to line group");
		},
		error:(req, status, err) => {
			alert("failed to send message");
		},
		complete: () => {
		}
	});
}

jQuery(()=>{
	console.log("load notify page");

	$("button#notify").click(() => {
		submit_notify();
	});
});
