#!/bin/php

<?php
$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw==";
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

$cdecode = base64_decode($cookie);

$dencode = json_encode($defaultdata);

$key = "";

for ($i=0;$i<strlen($cdecode);$i++)
{
    $temp = $cdecode[$i] ^ $dencode[$i];
    
    if (strpos($key,$temp)===False){
        $key .= $temp;
    }
    else{
        break;
}
}

function xor_encrypt($var,$key){

    $outtext = "";
    for ($i=0;$i<strlen($var);$i++)
    {
	$outtext .= $var[$i] ^ $key[$i % strlen($key)];
    }
    return $outtext;
}
$fdata = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

$cookie = base64_encode(xor_encrypt(json_encode($fdata),$key));

printf("Cookie = \"%s\"",$cookie);

#iterate through each string and xor each value with the corresponding in the other string
#check if char is already in key and append if not 
#break loop after a repeat is found 

#take key and use to encrypt a false cookie using showpassword = yes
#print the cookie ready to drop into python
?>


