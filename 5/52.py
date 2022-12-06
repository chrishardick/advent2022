#!/usr/bin/python3
#==========
# 52.py
#==========

import sys
import re

def print_stacks (s):

    ii = 0

    for i in s:

        ii += 1

        print ("%d: %s" % (ii, i))


stacks = []

stage_1 = True

lines = []

num_stacks = 0

err = 0

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    if len(line) == 0:          # skip blank lines
        continue


    if stage_1:
    
        if not (re.search (r'^ 1', line)):      # not the last line of stage 1

            lines.append(line)

        else:                                   # the last line of stage 1

            ll = line.split()                   # by default, splits by whitespace

            num_stacks = len(ll)

            for i in range(0,num_stacks):       # initialize with empty stacks
                stacks.append([])

            stage_1 = False

            while len(lines):
            
                l = lines.pop()

                len_l = len(l)

                stack_idx = 0

                for i in range (1,len_l,4):   # 1, 5, 9, ...

                    if stack_idx < len(stacks):

                        if l[i] != ' ':
                            stacks[stack_idx].append(l[i])

                        stack_idx += 1
                    else:
                        err += 1
    

            print_stacks(stacks)

    else:   # stage ii

        # move x from y to z

        instr = line.split()        # split by whitespace

        if len(instr) != 6:

            err += 1

            continue

        num_items   = int(instr[1])
        fr          = int(instr[3])
        to          = int(instr[5])

        if fr > num_stacks or to > num_stacks:
            err += 1

            continue

        fr -= 1     # indexed by 0
        to -= 1

        tmp_stack = []

        for i in range(num_items):

            tmp_stack.append(stacks[fr].pop())

        for i in range(num_items):

            stacks[to].append(tmp_stack.pop())

result = ""
for s in stacks:
    if len(s):
        result += s.pop()
    else:
        result += ""
   
print ("result=%s, #err=%d" % (result,err))
