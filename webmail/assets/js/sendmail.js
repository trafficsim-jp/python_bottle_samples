
function submit_message(){
	let message = $("textarea#mailmessageinput").val();
	let subject = $("input#mailsubject").val();

	console.log(subject);
	console.log(message);

	$.ajax({
		type: 'POST',
		contentType: 'application/json',
		dataType: 'json',
		url: RESTURIROOT+'/sendmail/sendmessage',
		data: JSON.stringify({ subject: subject, message:message }),
		success:(res) => {
			alert("success to send message");
		},
		error:(req,status,err) => {
			alert("failed to send message");
		},
		complete: () => {
		}
	});
}

jQuery(()=>{
	console.log("load sendmail.js");
	console.log(RESTURIROOT);

	$("button#sendmessage").click(()=>{
		submit_message();
	});
});
