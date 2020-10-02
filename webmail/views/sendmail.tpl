<%
from bottle import request
import assets
javascript_assets=assets.assets('js', 'sendmail.js')
url=request.urlparts.scheme+'://'+request.urlparts.netloc+'/api'
%>
<!DOCTYPER html>
<html>
  <head>
    <meta charset="utf-8">
    <title>sendmail</title>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
            integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
            crossorigin="anonymous"></script>
    <script type="text/javascript">
     const RESTURIROOT="{{!url}}"
    </script>
    {{!javascript_assets}}
    <style type="text/css">
     #mailmessageinput {
         width:100%;
         height:100px;
         resize:vertical;
     }
    </style>
  </head>
  <body>
    <fieldset>
      <legend>mail message</legend>
      <label>subject:</label>
      <input id="mailsubject" type="text" placeholder="subject"><br>
      <textarea name="mailmessageinput" type="text" id="mailmessageinput" placeholder="送信メッセージ"></textarea>
      <button id="sendmessage">send</button>
    </fieldset>
  </body>
</html>
