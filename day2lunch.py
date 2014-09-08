#!/usr/bin/env python

accepted_hits_fname = "/Users/cmdb/data/day1/accepted_hits.SAM"

f = open (accepted_hits_fname)

nl = 0
while True: 
    line = f.readline()
    if not line: 
        break
    else: 
        nl = nl + 1
print "Number of alignments " , nl 

#18417212

t = 0
while True: 
    line = f.readline()
    if "NM:i:1" in line: 
        t = t + 1
    else: 
        break
print "Number of perfect alignments ", t

u =0
for line in f:
    if "NH:i" not in line:
        break
    if "NH:i:1" in line:
        u = u + 1
print "Number of exactly one location reads", u

for i, line in enumerate(f):
    fields = line.rstrip ("\r\n"). split("\t")
    print fields [2]


    



