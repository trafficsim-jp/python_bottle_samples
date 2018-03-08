<!DOCTYPE html
<%
from bottle import request
import assets
javascript_assets=assets.assets('js','record.js')
url=request.urlparts.scheme+'://'+request.urlparts.netloc+'/api'
%>
<html>
<head>
    <meta charset="UTF-8">
    <title>MediaDevices.getUserMedia()</title>
	<script src="https://code.jquery.com/jquery-3.2.1.min.js" ></script>
	{{!javascript_assets}}
	<script type="text/javascript">
	 const RESTURIROOT="{{!url}}"
	</script>
</head>
<body>
	<p>
	<input type="button" onclick="startRecorder();" value="録音開始">
	<input type="button" onclick="exportWAV();" value="WAVファイル送信">
	</p>
	<p>
	<audio src="https://web-sandbox.trafficsim.co.jp:10443/getwav/upload.wav" controls>
		<p>音声を再生するには、audioタグをサポートしたブラウザが必要です。</p>
	</audio>
	</p>
</body>
</html>
