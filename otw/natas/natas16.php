#!/usr/bin/php
<?php
$key = $argv[1];
echo("key: ".$key."\n");

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        echo("Input contains an illegal character!\n");
    } else {
        echo("Query: grep -i \"$key\" dictionary.txt\n");
    }
    echo("Result: ");
    echo(passthru("grep -i \"$key\" dictionary.txt"));
    echo("\n");
}
?>
