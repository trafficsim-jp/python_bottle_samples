<!DOCTYPE html
<%
from bottle import request
import assets
javascript_assets=assets.assets('js','movpost.js')
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

<button onclick="startVideo()">ビデオ撮影開始</button>
<button onclick="stopVideo()">ビデオ撮影終了</button>
<button id="startflvideo">コマ送り撮影開始</button>
<button id="stopflvideo">コマ送り撮影終了</button>

<h2>動画</h2>
<video autoplay width="320" height="240"></video>

<h2>コマ送り</h2>
<img/>


<canvas style="display: none" width="320" height="240" id="myCanvas"></canvas>
</body>
</html>
