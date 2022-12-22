#!/usr/bin/python3
#==========
# 141.py
#==========

import sys
import re

class Solution:

    def __init__(self):

        # each entry is [(x,y), (x,y), ....]
        self.lines = []

        self.occupied = set()

        self.min_x = None
        self.max_x = None

        self.max_y = None


    # read stdin, populate self.lines[]

    def get_input (self):

        for line in sys.stdin:
        
            line = line.rstrip()        # remove any white space from end of string
        
            line = re.sub (r'->','',line)
        
            xy = line.split()
        
            coordinates = []
        
            for i in xy:
                x_y = i.split(r',')
        
                coordinates.append((int(x_y[0]),int(x_y[1])))
        
            self.lines.append(coordinates)

        self.draw_lines()
   

    # traverse self.lines[], populate self.occupied
    # - also populates min and max values

    def draw_lines (self):

        # for each line
        
        for line in self.lines:
            print ("\nline=",line)
        
        
            # for each xy coordinate
        
            last = None
        
            for xy in line:
           
                print ("xy=",xy)
            
                x = xy[0]
                y = xy[1]
        
                if last:
        
                    if last[0] == xy[0]:
                        # same x
        
                        start   = min(last[1],xy[1])
                        end     = max(last[1],xy[1]) + 1
        
                        for yy in range(start,end):
                            self.occupied.add((x,yy))
        
                    elif last[1] == xy[1]:
                        # same y
        
                        start   = min(last[0],xy[0])
                        end     = max(last[0],xy[0]) + 1
        
                        for xx in range(start,end):
                            self.occupied.add((xx,y))
        
                    else:
                        raise RuntimeError("invalid line")
        
                last = xy
        
                if not self.min_x or x < self.min_x:
                    self.min_x = x
        
                if not self.max_x or x > self.max_x:
                    self.max_x = x
        
                if not self.max_y or y > self.max_y:
                    self.max_y = y
        
        print ("min_x", self.min_x)
        print ("max_x", self.max_x)
        print ("max_y", self.max_y)

   
    def valid_x (self, x):
        if x >= self.min_x and x <= self.max_x:
            return True
        #print ("not a valid x",x)
        return False

    def valid_y (self, y):
        if y <= self.max_y:
            return True
        #print ("not a valid y",y)
        return False


    def run_simulation (self):

        num = 0     # number pieces of sand

        abyss = False

        while abyss == False:

            # starting point for each piece of sand
            x = 500
            y = 0

            while (True):

                if not (x,y+1) in self.occupied:

                    if not self.valid_y(y+1):
                        abyss = True
                        break

                    y += 1

                elif not (x-1,y+1) in self.occupied:

                    if not self.valid_x(x-1) or not self.valid_y(y+1):
                        abyss = True
                        break

                    x -= 1
                    y += 1

                elif not (x+1,y+1) in self.occupied:
                    
                    if not self.valid_x(x+1) or not self.valid_y(y+1):
                        abyss = True
                        break

                    x += 1
                    y += 1

                else:
                    # no place to go

                    self.occupied.add((x,y))
                    num += 1
                    print ("sand:",x,y,"#=",num)

                    break

        return num


#
# main
#

s = Solution()

s.get_input()

print ("result=",s.run_simulation())
