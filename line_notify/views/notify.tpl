<%
from bottle import request
import assets
javascript_assets=assets.assets('js', 'notify.js')
url=request.urlparts.scheme+'://'+request.urlparts.netloc+'/api'
%>

<!DOCTYPER html>
<html>
  <head>
    <meta charset="utf-8">
    <title>notify</title>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
            integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
            crossorigin="anonymous"></script>
    <script type="text/javascript">
     const RESTURIROOT="{{!url}}"
    </script>
    {{!javascript_assets}}
    <style type="text/css">
     textarea#notifymessage {
         width:100%;
         height:100px;
         resize:vertical;
     }
    </style>
  </head>
  <body>
    <fieldset>
      <textarea name="notify" type="text" id="notifymessage" placeholder="送信メッセージ"></textarea><br>
      <button id="notify">notify</button>
    </fieldset>
  </body>
</html>
