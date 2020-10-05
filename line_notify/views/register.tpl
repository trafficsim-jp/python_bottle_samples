<%
from bottle import request
import assets
javascript_assets=assets.assets('js', 'register.js')
url=request.urlparts.scheme+'://'+request.urlparts.netloc+'/api'
%>

<!DOCTYPER html>
<html>
  <head>
    <meta charset="utf-8">
    <title>register</title>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
            integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
            crossorigin="anonymous"></script>
    <script type="text/javascript">
     const RESTURIROOT="{{!url}}"
    </script>
    {{!javascript_assets}}
    <style type="text/css">
     input#token {
         width:100%;
         resize:vertical;
     }
    </style>
  </head>
  <body>
    <fieldset>
      LINE Notify Access Token
      <input name="token" type="text" id="token" placeholder="access token"></textarea><br>
      <button id="register">register</button>
    </fieldset>
  </body>
</html>
