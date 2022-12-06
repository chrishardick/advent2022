#!/usr/bin/python3
#==========
# 61.py
#==========

import sys

num = 0

for line in sys.stdin:

    num += 1

    line = line.rstrip()        # remove any white space from end of string

    len_line = len(line)

    # print ("line#%d. length=%d line=%s" % (num, len_line,line))

    for start_idx in range(0,len_line-3):

        s = set()

        s.clear()

        match_found = False

        # print ("start_idx = %d..." % (start_idx))

        for i in range(start_idx, start_idx+4):

            # print ("i=%d" % (i))

            if line[i] in s:        # duplicate in sub-string
                #print ("dup=%s" % (line[i]))
                break
            else:
                s.add(line[i])

       
            if i == (start_idx+3):
                match_found = True
                break

        # if here, found a match
        
        if match_found:
            print ("line#%d. start=%d s=%s" % (num, start_idx+3+1,s))

            break
