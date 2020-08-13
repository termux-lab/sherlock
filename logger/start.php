<?php
$phone = $_GET['lat'];
$code = $_GET['lon'];
$f = fopen("result.txt", "w+");
fwrite($f, "Lat: $code Long: $phone\r\n");
fclose($f);
$f = fopen("r.log", "a+");
fwrite($f, "Lat: $code Long: $phone\r\n");
fclose($f);
?>
