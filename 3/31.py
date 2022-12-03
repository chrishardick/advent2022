#!/usr/bin/python3
#==========
# 31.py 
#==========

import sys

err = 0
num_lines = 0

brk = []

for line in sys.stdin:

    num_lines += 1

    line = line.rstrip()

    l = len(line)

    if l % 2 != 0:

        err += 1

        print ("line#%d - not even number of characters" % (num_lines))
        continue

    ll = int(l/2)

    s1 = line[0:ll]
    s2 = line[ll:l]

    if len(s1) != len(s2):

        err += 1

        print ("line#%d - lengths are not equal" % (num_lines))
        continue

    d1 = {}

    d1.clear()

    for c1 in s1:

        d1[c1] = 1

    for c2 in s2:

        if c2 in d1:

            if len(brk) == num_lines-1:
                print ("dup for line %d is %s" % (num_lines,c2))
                brk.append(c2)
            elif brk[num_lines-1] != c2:
                err += 1

                print ("line#%d - already wrote to brk. char=%s" % (num_lines,c2))


sum = 0

for b in brk:

    if b.islower():
        sum += (ord(b) - ord('a') + 1)

    elif b.isupper():
        sum += (ord(b) - ord('A') + 27)

    else:
        print ("not upper or lower")
        err +=1
           
print ("sum=%d, err=%d" % (sum,err))
        
