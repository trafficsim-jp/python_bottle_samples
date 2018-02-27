<%
from bottle import request
import assets
javascript_assets=assets.assets('js','getmovpost.js')
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
        <p id="flmov">自動再生</h2>
		<img/>
    </body>
</html>
