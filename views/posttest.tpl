<%
from bottle import request
import assets
javascript_assets=assets.assets('js','posttest.js')
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
    <section>
          <input type="text" id="posttext" name="word">
          <input type="submit" id="button" value="post">
        <p id="output"></p>
    </section>
    </body>
</html>
