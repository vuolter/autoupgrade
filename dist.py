#!/usr/bin/python
from distutils.core import run_setup
import os
import glob

os.system("pandoc -f markdown -t rst -o README.txt README.markdown")

dist = run_setup("setup.py", ["sdist", "upload"])
try:
    f = open("dist/index.html", "w")
    f.write('<html><head><title>Links for yab</title></head><body>')
    f.write('<h1>Links for yab</h1>')
    for d in glob.glob('dist/*.tar.*'):
        f.write('<a href="%(file)s">%(file)s</a><br>' % { "file" : os.path.basename(d) })
    f.write('</body></html>')
finally:
        f.close()

os.system("rsync -rvp --delete --chmod=D+x,ugo+r dist/ backup@enduro_nas.local:/volume1/web/simple/autoupgrade/")
print "do a git commit , add tag and push!"
# Note, manually add link to yab in http://enduro_nas.local/simple/index.html

