#!/usr/bin/python3
#==========
# 82.py
#==========

import sys


def view_distance (lines, x, y, max_x, max_y):

    distance = []
    distance.append(0)
    distance.append(0)
    distance.append(0)
    distance.append(0)

    for xx in range (x+1,max_x):
        distance[0] += 1
        if lines[y][xx] >= lines[y][x]:
            break
    
    for xx in range (x-1,-1,-1):
        distance[1] += 1
        if lines[y][xx] >= lines[y][x]:
            break
    
    for yy in range (y+1,max_y):
        distance[2] += 1
        if lines[yy][x] >= lines[y][x]:
            break;
    
    for yy in range (y-1,-1,-1):
        distance[3] += 1
        if lines[yy][x] >= lines[y][x]:
            break;

    for d in distance:
        print (d)

    return distance[0] * distance[1] * distance[2] * distance[3]
    

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

max_visible_score = 0
visible_score = 0


for y in range(max_y):
    for x in range(max_x):

        print ("[%d,%d]" % (x, y))

        visible_score = view_distance (lines, x, y, max_x, max_y)

        print ("score = %d" % (visible_score))

        if visible_score > max_visible_score:
            max_visible_score = visible_score

print ("max_visible_score=%d" % (max_visible_score))
