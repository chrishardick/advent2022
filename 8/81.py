#!/usr/bin/python3
#==========
# 81.py
#==========

import sys


def is_visible_helper (lines, val, x, y, max_x, max_y, mode):

    if x < 0 or x > max_x-1:
        return True

    if y < 0 or y > max_y-1:
        return True

    if lines[y][x] >= val:
        return False

    if mode == "x+":
        if is_visible_helper(lines, val, x+1, y, max_x, max_y, mode):
            return True
    elif mode == "x-":
        if is_visible_helper(lines, val, x-1, y, max_x, max_y, mode):
            return True
    if mode == "y+":
        if is_visible_helper(lines, val, x, y+1, max_x, max_y, mode):
            return True
    elif mode == "y-":
        if is_visible_helper(lines, val, x, y-1, max_x, max_y, mode):
            return True

    return False


def is_visible (lines, val, x, y, max_x, max_y):

    if x == 0 or x == max_x-1:
        return True

    if y == 0 or y == max_y-1:
        return True


    if is_visible_helper(lines, val, x+1, y, max_x, max_y,"x+"):
        return True

    if is_visible_helper(lines, val, x-1, y, max_x, max_y,"x-"):
        return True

    if is_visible_helper(lines, val, x, y+1, max_x, max_y,"y+"):
        return True

    if is_visible_helper(lines, val, x, y-1, max_x, max_y,"y-"):
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

    
