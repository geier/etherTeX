etherTeX
========

etherTeX is supposed to provide real-time co-operative LaTeX
editing. For this it uses etherpad-lite (for editing), pdf.js (for viewing),
pdfLaTeX and PyEtherpadLite (for the glue).

[https://github.com/Pita/etherpad-lite][etherpad-lite]
[https://github.com/devjones/PyEtherpadLite][pyetherpad-lite]
[https://github.com/andreasgal/pdf.js/][pdf.js]

etherTex is very crude, hackish and brute-force approach to this problem.
At the moment, etherTex allows only editing one LaTeX Document.

A test install can be found at [http://brutus.lostpackets.de/ethertex/ethertex.py](http://brutus.lostpackets.de/ethertex/ethertex.py "test install") .

FAQ
---
**Why is there no pdf displayed?**
the LaTex document probably doesn't compile
**why can't I see any changes in the pdf?**
you need to manually hit the "typeset" button on the top left
**why is the pdf is not properly displayed?**
pdf.js is no perfect yet
**can I download the pdf?**
yes, at http://brutus.lostpackets.de/ethertex/pad.pdf

License
-------
I believe there isn't really anything here that deserves a license, but it
might become larger sooner. The stuff I wrote I herewith place under the
beer-ware license:

"THE BEER-WARE LICENSE" (Revision 42): Christian Geier wrote this file. As
long as you retain this notice you can do whatever you want with this stuff.
If we meet some day, and you think this stuff is worth it, you can buy me a
beer in return Christian Geier

this does not concern the pdf.js code that is included in this repository.
