#!/usr/local/bin/python

#EDIT
pdflatex = "/usr/local/texlive/2011/bin/amd64-freebsd/pdflatex"

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import os
import tempfile
import codecs

#EDIT
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

        <script type="text/javascript" src="compatibility.js"></script>
        <script type="text/javascript" src="viewer.js"></script>
        <script type="text/javascript" src="../pdf.js/pdf.js"></script>

        <script type="text/javascript" src="../pdf.js/fonts.js"></script>
        <script type="text/javascript" src="../pdf.js/crypto.js"></script>
        <script type="text/javascript" src="../pdf.js/glyphlist.js"></script>
  </head>

  <body>
    <div id="controls">
      <button id="previous" onclick="PDFView.page--;">

        <img src="images/go-up.svg" align="top" height="32"/>
        Previous
      </button>

      <button id="next" onclick="PDFView.page++;">
        <img src="images/go-down.svg" align="top" height="32"/>
        Next
      </button>

      <div class="separator"></div>

      <input type="text" id="pageNumber" onchange="PDFView.page = this.value;" value="1" size="4"></input>

      <span>/</span>
      <span id="numPages">--</span>

      <div class="separator"></div>

      <select id="scaleSelect" onchange="PDFView.scale = parseInt(this.value);">
        <option value="50">50%</option>

        <option value="75">75%</option>
        <option value="100">100%</option>
        <option value="125">125%</option>
        <option value="150" selected="selected"><p>150%</p></option>
        <option value="200">200%</option>
      </select>

      <div class="separator"></div>

      <input id="fileInput" type="file"></input>

      <div class="separator"></div>

      <span id="info">--</span>
    </div>

    <div id="sidebar">

      <div id="sidebarBox">
        <div id="sidebarScrollView">
          <div id="sidebarView"></div>
        </div>
     </div>
    </div>

    <div id="viewer"></div>
  </body>

</html>

"""
