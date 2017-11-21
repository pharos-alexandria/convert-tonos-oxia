#!/usr/bin/env python

import sys
import string

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, 'r') as fin:
    contents = fin.read()
     
with open(outfile, 'w') as fout:
    newcontents = contents.translate(str.maketrans("άέήίόύώ", "άέήίόύώ"))
    fout.write(newcontents)
