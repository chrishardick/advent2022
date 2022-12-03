#!/usr/bin/python3
#==========
# 2_2.py
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

        if line[0] == 'A':          # opponent=rock

            if line[2] == 'X':      # LOSE

                score += 0
                score += 3          # scissors


            elif line[2] == 'Y':    # DRAW

                score += 3
                score += 1          # rock


            elif line[2] == 'Z':    # WIN

                score += 6
                score += 2          # paper

            else:

                invalid_lines += 1
            

        elif line[0] == 'B':        # opponent=paper

            if line[2] == 'X':      # LOSE

                score += 0
                score += 1          # rock


            elif line[2] == 'Y':    # DRAW

                score += 3
                score += 2          # paper


            elif line[2] == 'Z':    # WIN

                score += 6
                score += 3          # scissors

            else:

                invalid_lines += 1
            

        elif line[0] == 'C':        # opponent=scissors

            if line[2] == 'X':      # LOSE

                score += 0
                score += 2          # paper


            elif line[2] == 'Y':    # DRAW

                score += 3
                score += 3          # scissors


            elif line[2] == 'Z':    # WIN

                score += 6
                score += 1          # rock

            else:

                invalid_lines += 1
            


        else:

            invalid_lines += 1

print ("score=%d, num_lines=%d, invalid_lines=%d" % (score,num_lines,invalid_lines))
