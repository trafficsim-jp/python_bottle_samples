<%
from bottle import request
import assets
javascript_assets=assets.assets('js','picpost.js')
url=request.urlparts.scheme+'://'+request.urlparts.netloc+'/api'
%>
<html>
<head>
	<meta charset="UTF-8">
	<title>MediaDevices.getUserMedia()</title>
</head>
<body>

<!--<button id="image_select">画像選択</button><br>ボタンでできるかどうか確認する-->
<input type="file" id="image_select"><br>
<h2>選択した写真</h2>

<div id = "pre_image">
</div><br>

<!--<canvas id="pre_image" width="320" height="240"></canvas><br><br>-->

<button id="object_detection">物体検出</button>
<h2>画像認識後</h2>

<div id = "post_image">
</div>

<script src="https://code.jquery.com/jquery-3.2.1.min.js" ></script>
{{!javascript_assets}}
<script type="text/javascript">
 const RESTURIROOT="{{!url}}"
</script>

</body>
</html>
