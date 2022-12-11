#!/usr/bin/python3
#==========
# 102.py
#==========

import sys

def print_val (cycle, reg):

    #           1         2         3         
    # 0123456789012345678901234567890123456789

    # cycle is ever increasing starting from 1
    # - 40 pixels per line (0-39)

    # pixel goes from 0-39 
    pixel = (cycle - 1) % 40

    val = '.'

    # register value is center of sprite
    # - sprite is 3 wide at [reg-1, reg+1]
    if (pixel == reg-1 or pixel == reg or pixel == reg+1): 
        val = '#'

    print (val,sep="",end="")
        
    if pixel == 39:
        print ("EOL")
        

cycle = 0   # cycle number

reg = 1     # registry value

num = 0     # line number

tot = 0

for line in sys.stdin:

    num += 1

    line = line.rstrip()        # remove any white space from end of string

    # print ("line=%s" % (line))

    flds = line.split()

    if flds[0] == "noop":

        cycle += 1
        print_val (cycle, reg)

        # print ("CYCLE=%d noop REG=%d" % (cycle, reg))

    elif flds[0] == "addx":

        cycle += 1
        print_val (cycle, reg)

        # print ("CYCLE=%d addx1. REG=%d" % (cycle, reg))


        cycle += 1
        print_val (cycle, reg)
       
        val = int(flds[1])

        # print ("CYCLE=%d addx2. val=%d - REG=%d" % (cycle, val, reg))

        reg += val
        
    else:
        raise RuntimeError ("Invalid Line |%s|" % (line))

