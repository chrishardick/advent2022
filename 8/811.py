#!/usr/bin/python3
#==========
# 811.py
#==========

import sys


def is_visible (lines, val, x, y, max_x, max_y):

    if x == 0 or x == max_x-1:
        return True

    if y == 0 or y == max_y-1:
        return True

    # 

    visible = True

    for xx in range (x+1,max_x):
        if lines[y][xx] >= lines[y][x]:
            visible = False
            break

    if visible:
        return True


    #

    visible = True

    for xx in range (x-1,-1,-1):
        if lines[y][xx] >= lines[y][x]:
            visible = False
            break

    if visible:
        return True


    #

    visible = True

    for yy in range (y+1,max_y):
        if lines[yy][x] >= lines[y][x]:
            visible = False
            break

    if visible:
        return True
   

    # 
    
    visible = True

    for yy in range (y-1,-1,-1):
        if lines[yy][x] >= lines[y][x]:
            visible = False
            break

    if visible:
        return True
   
    return False


#
# main
#

lines = []

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    lines.append(line)


max_x = len(lines[0])
max_y = len(lines)

print ("max_x=%d, max_y=%d" % (max_x,max_y))

num_visible = 0

for y in range(max_y):
    for x in range(max_x):
        if is_visible(lines, lines[y][x], x, y, max_x, max_y):
            num_visible += 1
            print ("#%d val=%d x=%d y=%d is visible" % (num_visible, int(lines[y][x]), x, y))

print ("num_visible=%d" % (num_visible))

    
