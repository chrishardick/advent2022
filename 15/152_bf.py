#!/usr/bin/python3
#==========
# 152_bf.py
# - brute force
#==========

import sys
import re

class Sensor:

    mx = 0

    def __init__ (self, xy, b_xy):

        self.xy         = xy
        self.b_xy       = b_xy

        self.length     = abs(self.xy[0] - self.b_xy[0]) + abs(self.xy[1] - self.b_xy[1])

        self.min_y      = self.xy[1] - self.length
        self.max_y      = self.xy[1] + self.length


    def __str__ (self):

#        return (    "s=%s,b=%s,l=%d" %
#                    (self.xy, self.b_xy, self.length)
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

        if start_x < 0:
            start_x = 0

        stop_x = self.xy[0] + width + 1

        if stop_x > Sensor.mx+1:
            stop_x = Sensor.mx+1

        #print ("\twidth=",width,"start_x=",start_x,"stop_x=",stop_x)

        for i in range(start_x,stop_x):
            ret.add(i)

        #print ("\tret=",ret)
        return ret
            

        
# main

Sensor.mx = 20

if len(sys.argv) >= 2:
    Sensor.mx = int(sys.argv[1])

print ('max=',Sensor.mx)


# Sensor list
sensors = []

# Read input, populate Sensor list
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


X = Y = None

for i in range(Sensor.mx+1):

    row = set()

    #if i%10==0 or i==Sensor.mx:
    print ("Row:",i,"...")

    for s in sensors:

        #print ("\t",s)
        row |= s.row_map(i)

    if len(row) < Sensor.mx+1: 
        print ("match!",i,row)

        Y = i

        for j in range (Sensor.mx+1):
            if not j in row:
                X = j
                break

result = X*4000000+Y
print ( "X=", X
        ,"Y=",Y
        ,"result=",result
        )
