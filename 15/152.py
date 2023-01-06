#!/usr/bin/python3
#==========
# 152.py
#==========

import sys
import re

import gc

from sensor import Sensor 

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

# the answer must lie at a peripheral location
# - construct a set of all the peripheral locations
pset = set()

for s in sensors:

    i += 1

    print ("i=",i,"sensor=",s)

    pset |= s.peripheral_set()
    print ("cumulative set size=",len(pset),"\n")

    print ("gc...",end="")
    gc.collect()
    print ("done")

print ("done calculating peripheral set. size=",len(pset))

X = Y = None

# go thru all peripheral points 
# - look for a location which is not in coverage area

# for each peripheral point
for i in pset:

    location_found = True

    for s in sensors:
        if s.in_coverage_area(i[0],i[1]):
            location_found = False
            break

    if location_found:
        X = i[0]
        Y = i[1]

        print ("location found!", X, Y)
        break

if X == None or Y == None:
    print ("not found")
    sys.exit(-1)

result = X*4000000+Y
print ( "X=", X
        ,"Y=",Y
        ,"result=",result
        )
