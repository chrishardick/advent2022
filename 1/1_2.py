#!/usr/bin/python3
#==========
# 1_2.py
#
# how many calories does that elf have
#==========

import sys

import heapq

m = 0

x = 0

num = 0

l = []

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    if not line:

        # end of an elf

        l.append(x)

        x = 0

    else:
    
        x += int(line)

l.sort(reverse=True)


lll = 0

tot = 0

for ll in l:

    print ("%d" % (ll))

    lll += 1

    tot += ll

    if lll == 3:
        print ("total=%d" % (tot))
        break


