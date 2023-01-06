#!/usr/bin/python3
#==========
# sensor.py
#==========

import sys
import re

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
 

        #print ("peripheral_set:")

        #for r in sorted(ret):
        #    print (r)

        return ret

    # return boolean as to whether or not point is in coverage area
    def in_coverage_area (self, x, y):

        if not self.valid_pt(x,y):
            raise RuntimeError ("invalid point")

        if y < self.min_y or y > self.max_y:
            return False

        row_diff = abs(y-self.xy[1])
        width = self.length - row_diff

        rel_min_x = self.xy[0]-width
        rel_max_x = self.xy[0]+width

        if x < rel_min_x or x > rel_max_x:
            return False

        return True
