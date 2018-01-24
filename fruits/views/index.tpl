<%
from bottle import request
import assets
javascript_asstes=assets.assets('js','index.js')
url=request.urlparts.scheme+'://'+request.urlparts.netloc+'/api'
%>
<html>
    <head>
	<meta charset="utf-8">
	<title>index</title>
	<script src="https://code.jquery.com/jquery-3.2.1.min.js" ></script>
	{{!javascript_asstes}}
	<script type="text/javascript">
	 const RESTURIROOT="{{!url}}"
	</script>
    </head>
    <body>
	<p id="fruitsbox">未だもらっていない</p>
	<button id="reget">再取得</button>
    </body>
</html>
