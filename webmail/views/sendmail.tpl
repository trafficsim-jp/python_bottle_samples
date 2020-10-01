<!DOCTYPER html>
<html>
  <head>
    <meta charset="utf-8">
    <title>sendmail</title>
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
      <form name="mailmessage">
        <textarea name="mailmessageinput" type="text" id="mailmessageinput" placeholder="送信メッセージ"></textarea>
        <button id="sendbtn">send</button>
      </form>
    </fieldset>
  </body>
</html>
