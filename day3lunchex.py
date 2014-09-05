#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it. 
"""

import sys

line = sys.stdin.readline()
#assert ">" in line
sid = line[1:].rstrip("\r\n")

sample =[]
while 1: 
    line = sys.stdin.readline()
    if line == "":
        break 
#    if "Queries = 28" in line:
#        print line.rstrip()

        
    if ">" in line or line.startswith ("Query="): 
        name =  line.rstrip("\r\n")
    if "Identities" in line: 
        identities = line.rstrip("\r\n").split()[2]
          
        print name, identities 
#        sequence_name = line[1:].rstrip("\r\n").strip("\t")
    
    
#    elif ">" not in line:
#        break
                


