#!/usr/bin/env python2

import sys

if len(sys.argv) != 3:
    print "need 2 args!"
    sys.exit(-1)

database = open(sys.argv[1], "r")
lines = database.readlines()

# take 3 lines and put them into list -> reapeat
title_link_pairs = [lines[x:x+3] for x in xrange(0, len(lines), 3)]

# get out last element (it's empty line)
map(lambda x: x.pop(), title_link_pairs)

# constructs hrefs
hrefs = []
for pair in title_link_pairs:
    if len(pair) != 2:
        continue
    hrefs.append('<li><a href="%s">%s</a></li>' % (pair[1], pair[0]))

# construct html code
html = "<html>\n<body>\n</div>\n<ul>"
for i in hrefs:
    html += i + '\n'
html += "</ul></div></body></html>"

# save to html file
html_file = open(sys.argv[2], "w")
html_file.write(html)
html_file.close()

print "done"
sys.exit(0)
