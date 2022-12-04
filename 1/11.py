#!/usr/bin/python3
#==========
# 11.py
#
# how many calories does that elf have
#==========

import sys

m = 0

x = 0

num = 0

for line in sys.stdin:

    line = line.rstrip()    # remove any white space from end of string

    if not line:

        # end of an elf

        num += 1

        if x > 0:
            if x > m:
                m = x

        x = 0

    else:
    
        x += int(line)


print ("num elfs = %d" % (num))
print ("max = %d" % (m))

