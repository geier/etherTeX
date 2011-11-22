#!/usr/local/bin/python
pdflatex = "/usr/local/texlive/2011/bin/amd64-freebsd/pdflatex"
import cgi 
import cgitb; cgitb.enable()  # for troubleshooting
import os
import tempfile
import codecs

from py_etherpad import EtherpadLiteClient
myPad = EtherpadLiteClient('yourapitoken','http://etherpad.install.tld/api')

#get the text of the etherpad
padText = myPad.getText('testPad')

tmpDir= tempfile.mkdtemp()

# Clean up the directory yourself
# os.removedirs(tmpDir)

file = codecs.open("%s/pad.tex" %(tmpDir), "w", "utf-8")
#print "%s/pad.tex" %(tmpDir)
file.write(padText['text'])
file.close()

#cmdstring = "some_other_script.py %s %s" % (argument1 argument2)
cmdstring = "%s -output-directory=%s -halt-on-error %s/pad.tex > /dev/null" %(pdflatex,tmpDir,tmpDir)
os.system(cmdstring)
cmdstring = "cp %s/pad.pdf ." % (tmpDir)
os.system("rm pad.pdf")
os.system(cmdstring)
os.system("rm %s/pad*" % (tmpDir))
#os.removedirs(tmpDir)



print "Content-Type: text/html"
print
print """
<!DOCTYPE html>
<html>
    <head>
        <title>Simple pdf.js page viewer</title>
        <link rel="stylesheet" href="viewer.css"></link>

	  <script type="text/javascript" src="pdf.js"></script>

	  <script type="text/javascript">
	    // Specify the main script used to create a new PDF.JS web worker.
	    // In production, change this to point to the combined `pdf.js` file.
	    PDFJS.workerSrc = 'pdf.js';
	  </script>
	  <script type="text/javascript" src="custom.js"></script>
  </head>

  <body>
  <canvas id="the-canvas" style="border:1px solid black;"/>
  </body>
</html>

"""
