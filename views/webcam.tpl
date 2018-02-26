<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>MediaDevices.getUserMedia()</title>
</head>
<body>

<button onclick="startVideo()">ビデオ撮影開始</button>
<button onclick="stopVideo()">ビデオ撮影終了</button>
<button onclick="snapshot()">写真撮影</button>
<button onclick="saveCanvas()">スナップショットを保存</button>

<h2>動画</h2>
<video autoplay width="320" height="240"></video>

<h2>スナップショット</h2>
<img/>


<canvas style="display: none" width="320" height="240" id="myCanvas"></canvas>
<script src="../assets/js/webcam.js"></script>
</body>
</html>
