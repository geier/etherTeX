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
<form>
<button id="typeset">typeset</button>
</form>
</div>


<iframe id="pdfframe" src="pdfjs.py" width=48% height=800px> 
</iframe>
<iframe id="etherframe" src="http://lostpads.de/p/testPad?showControls=true&showChat=true&showLineNumbers=true&useMonospaceFont=false" width=48% height=800px>
</iframe>

    </body>
</html>
"""
