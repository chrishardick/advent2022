#!/usr/bin/python3
#==========
# 152.py
#==========

import sys
import re

import gc

class Sensor:

    mx = 0

    pset = set()

    def __init__ (self, xy, b_xy):

        self.xy         = xy
        self.b_xy       = b_xy

        self.length     = abs(self.xy[0] - self.b_xy[0]) + abs(self.xy[1] - self.b_xy[1])

        self.min_x      = self.xy[0] - self.length
        self.max_x      = self.xy[0] + self.length

        self.min_y      = self.xy[1] - self.length
        self.max_y      = self.xy[1] + self.length


    def __str__ (self):

#        return (    "s=%s,b=%s,l=%d" %
#                    (self.xy, self.b_xy, self.length)
#                    )

        return (    "s=%s,b=%s,l=%d,min_y=%d,max_y=%d" %
                    (self.xy, self.b_xy, self.length, self.min_y, self.max_y)
                    )

    def valid_pt (self, x, y):

        if x < 0 or x > Sensor.mx:
            return False

        if y < 0 or y > Sensor.mx:
            return False

        return True

    # return set of peripheral coordinates
    def peripheral_set (self):
      
        ret = set()

        if self.valid_pt(self.xy[0],self.min_y-1):
            ret.add((self.xy[0],self.min_y-1))

        if self.valid_pt(self.xy[0],self.max_y+1):
            ret.add((self.xy[0],self.max_y+1))

        min_y = self.min_y

        if min_y < 0:
            min_y = 0

        for row in range (min_y,self.max_y+1):
        
            if row > Sensor.mx:
                break

            row_diff = abs(row-self.xy[1])
            width = self.length - row_diff

            x_left  = self.xy[0]-width-1
       
            if self.valid_pt(x_left,row):
                ret.add((x_left,row))
                
            x_right = self.xy[0]+width+1
                
            if self.valid_pt(x_right,row):
                ret.add((x_right,row))
   
        for r in sorted(ret):
            print (r)

        return ret

    # return boolean as to whether or not point is in coverage area
    def in_coverage_area (self, x, y):

        if not self.valid_pt(x,y):
            raise RuntimeError ("invalid point")

        row_diff = abs(y-self.xy[1])
        width = self.length - row_diff

        rel_min_x = self.xy[0]-width
        rel_max_x = self.xy[0]-width

        if x < rel_min_x or x > rel_max_x:
            return False

        return True

        
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


print ("calculating peripheral set...")

i=0

pset = set()

for s in sensors:

    i += 1

    print ("i=",i,"sensor=",s)

    ret = s.peripheral_set()
    pset |= ret

    print ("size=",len(ret),"\n")

print ("done calculating peripheral set. size=",len(pset))

print ("final set=")
for ps in sorted(pset):
    print (ps)

X = Y = None

for i in pset:

    location_found = True

    for s in sensors:
        if s.in_coverage_area(i[0],i[1]):
            location_found = False
            break

    if location_found:
        X = i[0]
        Y = i[1]
        break

if X == None or Y == None:
    print ("not found")
    sys.exit(-1)

result = X*4000000+Y
print ( "X=", X
        ,"Y=",Y
        ,"result=",result
        )
