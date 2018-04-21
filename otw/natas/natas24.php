<html>
<head>
<body>
<h1>natas24</h1>
<div id="content">

Password:
<form name="input" method="get">
   <input type="text" name="passwd" size=20>
   <input type="submit" value="Login">
</form>

<?php
   if(array_key_exists("passwd",$_REQUEST)){
       if(strcmp($_REQUEST["passwd"],"kdm45dmdy3") == FALSE){
           echo "<br>The credentials for the next level are:<br>";
           echo "<pre>Username: natas25 Password: <censored></pre>";
       }
       else{
           echo(strcmp($_REQUEST["passwd"],"kdm45dmdy3"));
           echo "<br>Wrong!<br>";
       }
   }
   // morla / 10111
?>
</div>
</body>
</html>
