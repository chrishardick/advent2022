#!/usr/bin/python3
#==========
# driver.py
#==========

import sys
import re

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

    ret = s.peripheral_set()
    pset |= ret

    print ("size=",len(ret),"\n")

    for y in range(Sensor.mx):

        print ("%03d " % (y),end="")

        for x in range(Sensor.mx):
            if s.in_coverage_area(x,y):
                print ('X',end="")
            else:
                print ('.',end="")
        print ("")
