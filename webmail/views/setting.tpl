<%
from bottle import request
import assets
javascript_assets=assets.assets('js', 'setting.js')
url=request.urlparts.scheme+'://'+request.urlparts.netloc+'/api'
%>
<!DOCTYPER html>
<html>
  <head>
    <meta charset="utf-8">
    <title>setting</title>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
            integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
            crossorigin="anonymous"></script>
    <script type="text/javascript">
     const RESTURIROOT="{{!url}}"
    </script>
    {{!javascript_assets}}
  </head>
  <body>
    <fieldset>
      <legend>Server Setting</legend>
      smtp server:<br>
      <input id="smtp_server" type="text" placeholder="no setting"><br>
      port number:<br>
      <input id="smtp_port" type="number" placeholder="no setting"><br>
      user name(acount name of smtp server):<br>
      <input id="inputusername" type="text" placeholder="no setting"><br>
      password:<br>
      <input id=password" type="password" placeholder="no setting"><br>
      <br><button id="server_setting">submit</button>
    </fieldset>
    <fieldset>
      <legend>Address Setting</legend>
      from address:<br>
      <input id="from_address" type="text" placeholder="no setting"><br>
      destination addresses:<br>
      <input id="dest_addresses" type="text" placeholder="no setting"><br>
      <br><button id="address_setting">submit</button>
    </fieldset>
  </body>
</html>
