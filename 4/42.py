#!/usr/bin/python3
#==========
# 42.py 
#==========

import sys

err = 0
num_lines = 0
contains_overlap = 0

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

    if (w00 <= w11 and w10 <= w01):
        contains_overlap += 1

print ("contains_overlap = %d, num_lines = %d, err=%d" % (contains_overlap, num_lines, err))
