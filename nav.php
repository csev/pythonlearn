<?php
function navto($arg)
{
  $uri = isset($_ENV["REQUEST_URI"]) ? $_ENV["REQUEST_URI"] : $_SERVER["REQUEST_URI"];
  echo ('href="' . $arg . '"');
  if ( strpos($uri, $arg) )  echo ' class="selected" ';
}
?>



<div class="title-bar hide-for-large">
  <div class="title-bar-left">
    <h1 class="menu-text"><a href="index.php" rel="nofollow" accesskey=1>PythonLearn</a></h1>
  </div>
  <div class="title-bar-right">
    <h1 id="menu-button" onclick="$('.mobile-menu').toggle()"><i class="fa fa-bars"></i></h1>
  </div>
         <div class="mobile-menu" style="display:none;">
               <ul class="no-bullet text-center">
<!--
                  <li><a <?php navto("book.php") ?> >Book</a></li>
                  <li><a <?php navto("install.php") ?> >Install</a></li>
-->
                  <li><a href=http://www.pr4e.org/ target="_blank">Coursera</a></li>
                  <li><a href="http://www.dr-chuck.com/" target="_blank">Instructor</a></li>
                  <li><a href="http://www.python.org/" target="_blank">Python</a></li>
                  <li><a <?php navto("about2.php") ?> >About</a></li>
               </ul>
         </div>
</div>


<div class="top-bar show-for-large">
        <div class="top-bar-left">
                <ul class="menu">
                        <li class="menu-text">
                                <a href="index.php" rel="nofollow" accesskey=1>PythonLearn</a>
                        </li>  
            </ul>
        </div>
        <div class="top-bar-right">
               <ul class="menu">
<!--
                  <li><a <?php navto("book.php") ?> >Book</a></li>
                  <li><a <?php navto("install.php") ?> >Install</a></li>
-->
                  <li><a href=http://www.pr4e.org/ target="_blank">Coursera</a></li>
                  <li><a href="http://www.dr-chuck.com/" target="_blank">Instructor</a></li>
                  <li><a href="http://www.python.org/" target="_blank">Python</a></li>
                  <li><a <?php navto("about2.php") ?> >About</a></li>
               </ul>         
         </div>
</div>
