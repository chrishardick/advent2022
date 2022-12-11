#!/usr/bin/python3
#==========
# 101.py
#==========

import sys

def signal_cycle (cycle):
    
    if cycle == 20:
        return True

    cycle -= 20

    if cycle % 40 == 0:
        return True

    return False


cycle = 0   # cycle number

reg = 1     # registry value

num = 0     # line number

tot = 0

for line in sys.stdin:

    num += 1

    line = line.rstrip()        # remove any white space from end of string

    print ("line=%s" % (line))

    flds = line.split()

    if flds[0] == "noop":

        cycle += 1

        print ("CYCLE=%d noop REG=%d" % (cycle, reg))

        if signal_cycle(cycle):
            strength = cycle * reg
            print ("signal cycle. cycle=%d REG=%d. strength=%d" % (cycle, reg, strength))
            tot += strength

    elif flds[0] == "addx":

        cycle += 1

        print ("CYCLE=%d addx1. REG=%d" % (cycle, reg))

        if signal_cycle(cycle):
            strength = cycle * reg
            print ("signal cycle. cycle=%d REG=%d. strength=%d" % (cycle, reg, strength))
            tot += strength

        cycle += 1
       
        val = int(flds[1])

        print ("CYCLE=%d addx2. val=%d - REG=%d" % (cycle, val, reg))

        if signal_cycle(cycle):
            strength = cycle * reg
            print ("signal cycle. cycle=%d REG=%d. strength=%d" % (cycle, reg, strength))
            tot += strength

        reg += val
        
    else:
        raise RuntimeError ("Invalid Line |%s|" % (line))

    print ("")

print ("TOTAL=%d" % (tot))
        

