#!/usr/local/bin/python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print "Content-Type: text/html"
print
print """
<!DOCTYPE html>
<html>
    <head>
	<title>real-time collaborative latex editing</title>
<script src="http://code.jquery.com/jquery-latest.js"></script>
    <script type="text/javascript">

        $(document).ready(function() {
            $('#typeset').click(function() {
                $('#pdfframe').attr('src', $('#pdfframe').attr('src'));
                return false;
            });
        });

    </script>
    </head>
    <body>
<div>
<div style="float:left">
<form>
<button id="typeset">typeset</button>
</form>
</div>
<div style="float:right">
<p>
<b>feel free to play around!</b>
<a href="faq.html">FAQ</a>
<a href="http://github.com/geier/ethertex">github</a>
<a href="http://brutus.lostpackets.de/ethertex/pad.pdf" id="button-download">download pdf</a></p>
</div>

</div>
<div style="clear:both;"></div>

<iframe id="pdfframe" src="pdfjs.py" width=48% height=800px> 
</iframe>
<iframe id="etherframe" src="http://lostpads.de/p/testPad?showControls=false&showChat=true&showLineNumbers=true&useMonospaceFont=false" width=48% height=800px>
</iframe>

    </body>
</html>
"""
