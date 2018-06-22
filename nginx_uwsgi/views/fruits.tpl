<%
from bottle import request
import assets
javascript_assets=assets.assets('js','fruits.js')
url=request.urlparts.scheme+'://'+request.urlparts.netloc+'/api'
%>
<html>
    <head>
        <meta charset="utf-8">
        <title>index</title>
        <script src="https://code.jquery.com/jquery-3.2.1.min.js" ></script>
        {{!javascript_assets}}
        <script type="text/javascript">
         const RESTURIROOT="{{!url}}"
        </script>
    </head>
    <body>
		<p>{{message}}</p>
		<p>{{!message}}</p>
        <p id="fruitsbox">未だもらっていない</p>
        <button id="reget">再取得</button>
    </body>
</html>
