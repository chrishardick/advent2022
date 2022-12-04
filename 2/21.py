#!/usr/bin/python3
#==========
# 21.py
#==========

import sys

score = 0
invalid_lines = 0
num_lines = 0

for line in sys.stdin:

    num_lines += 1

    line = line.rstrip()

    if len(line) != 3:

        invalid_lines += 1

    else:

        if line[2] == 'X':      # rock

            score += 1

            if line[0] == 'A':      # rock - tie

                score += 3

            elif line[0] == 'B':    # paper - loss

                score += 0

            elif line[0] == 'C':    # scissors - win

                score += 6

            else:

                invalid_lines += 1
            

        elif line[2] == 'Y':    # paper

            score += 2

            if line[0] == 'A':      # rock - win

                score += 6

            elif line[0] == 'B':    # paper - tie

                score += 3

            elif line[0] == 'C':    # scissors - loss

                score += 0
            
            else:

                invalid_lines += 1
           

        elif line[2] == 'Z':    # scissors

            score += 3
            

            if line[0] == 'A':      # rock - loss

                score += 0

            elif line[0] == 'B':    # paper - win

                score += 6

            elif line[0] == 'C':    # scissors - tie

                score += 3
      
            else:

                invalid_lines += 1

        else:

            invalid_lines += 1

print ("score=%d, num_lines=%d, invalid_lines=%d" % (score,num_lines,invalid_lines))
