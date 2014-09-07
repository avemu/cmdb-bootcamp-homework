#!/usr/bin/env python

import sys
import pandas as pd

#cufflinks_output = "/Users/cmdb/data/day4/transcripts.gtf"
#df = pd.read_table(cufflinks_output, header=None)

#if df[2].str.contains("transcript") and df[6] == "+":
#    print df
#else:
#    break

#line = df[3] + ' '+ df[0] 
chr_sizes ={'2L' :'23011544', 
'2LHet': '368872', 
'2R':  '21146708', 
'2RHet': '3288761', 
'3L':  '24543557', 
'3LHet': '2555491', 
'3R': '27905053', 
'3RHet': '2517507', 
'4': '1351857', 
'U': '10049037', 
'Uextra': '29004656', 
'X': '22422827', 
'XHet': '204112', 
'YHet': '347038', 
'dmel_mitochondrion_genome': '19517'}


#transcripts = df[2].str.contains("transcript")
#print line

name_chrsize = []
while 1:
    line = sys.stdin.readline().split()
    if len(line) == 0:
        break
#    if line[0] == line[0] in chr_sizes:
    if chr_sizes.has_key(line[0]) and '+' in line and 'transcript' in line:
        name_chrsize.extend([(line[0], line [3], chr_sizes.get(line[0]))])
    print name_chrsize
#    elif "-" in line: 
#        print line          