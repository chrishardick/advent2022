#!/usr/bin/python3
#==========
# 41.py 
#==========

import sys

err = 0
num_lines = 0
fully_contained = 0

for line in sys.stdin:

    num_lines += 1

    line = line.rstrip()

    s = line.split(",")

    if len(s) != 2:

        err += 1
        continue


    w0 = s[0].split("-")
    w1= s[1].split("-")

    if len(w0) != 2 or len(w1) != 2:

        err += 1
        continue

    w00 = int(w0[0])
    w01 = int(w0[1])

    w10 = int(w1[0])
    w11 = int(w1[1])

    if ((w00 <= w10 and w01 >= w11) or
        (w10 <= w00 and w11 >= w01)):

        fully_contained += 1

print ("fully_contained = %d, num_lines = %d, err=%d" % (fully_contained, num_lines, err))
