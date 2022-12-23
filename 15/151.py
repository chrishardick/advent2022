#!/usr/bin/python3
#==========
# 151.py
#==========

import sys
import re

class Sensor:

    def __init__ (self, xy, b_xy):

        self.xy         = xy
        self.b_xy       = b_xy

        self.length     = abs(self.xy[0] - self.b_xy[0]) + abs(self.xy[1] - self.b_xy[1])

        self.min_y      = self.xy[1] - self.length
        self.max_y      = self.xy[1] + self.length

    def __str__ (self):

#        return (    "s=%s,b=%s" %
#                    (self.xy, self.b_xy)
#                    )

        return (    "s=%s,b=%s,l=%d,min_y=%d,max_y=%d" %
                    (self.xy, self.b_xy, self.length, self.min_y, self.max_y)
                    )

    # given a row, return set
    def row_map (self,row):

        ret = set()

        if row < self.min_y or row > self.max_y:
            return ret

        row_diff = abs(row-self.xy[1])
        width = self.length - row_diff

        start_x = self.xy[0] - width
        stop_x  = self.xy[0] + width + 1

        print ("\twidth=",width,"start_x=",start_x,"stop_x=",stop_x)

        for i in range(start_x,stop_x):
            ret.add(i)

        return ret
            

        
#
# main
#

row = 10

if len(sys.argv) >= 2:
    row = int(sys.argv[1])

print ('row=',row)

sensors = []

beacons = set()


for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    match = re.search ( r'Sensor at x=(.*?), y=(.*?): closest beacon is at x=(.*?), y=(.*?$)'
                        ,line
                        )

    if not match:
        raise RuntimeError ("Invalid Line")

    s_x = int(match.group(1))
    s_y = int(match.group(2))

    b_x = int(match.group(3))
    b_y = int(match.group(4))

    sensors.append(Sensor((s_x,s_y),(b_x,b_y)))

    if (b_y == row):
        beacons.add(b_x)

res = set()

for s in sensors:
    xx = s.row_map(row)

    print (s, xx)

    res |= xx

res -= beacons

print (len(res))
