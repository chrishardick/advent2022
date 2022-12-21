#!/usr/bin/python3
#==========
# 131.py
#==========

# pairs of packets
# how many pairs of packets are are in the correct order
#
# lists and integers
# - each list starts with [ and ends with ]
# - each packet is always a list and appears on its own line
#
# if both values are integers, the lower integer should come 1st
# - if both values are the same integer, continue checking the next part of the input
#
# if both values are lists, compare each item in the list to its respective item in the other list
# if the left list runs out of items -> right order
# if the right list runs out of items -> not the right order
# if lists are the same length and no decision, continue checking the next part of the input
#
# if list vs. integer, convert the integer to a list and retry the comparison
#
# return the sum of the indexes in the correct order
'''
[1,1,3,1,1]
[1,1,5,1,1]     -> correct order

[[1],[2,3,4]]
[[1],4]         -> correct order

[9]
[[8,7,6]]       -> not in correct order

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1, [2,[3,[4,[5,6,7]]]], 8, 9]
[1, [2,[3,[4,[5,6,0]]]], 8, 9]
'''

import sys

class Expression:

    def __init__(self, value=""):

        self.value = value


    def handle_list (self):

        idx = 0

        buf = ""

        stack = []

        # [1,[2,[3,[4,[5,6,7]]]],8,9]
        # [
        # stack=[

        while idx < len(self.value):
      
            c = self.value[idx]
            idx += 1

            buf += c

            if c == '[':
                stack.append(c)
            elif c == ']':
                stack.pop()
                if len(stack) == 0:
                    break

        self.value = buf[1:len(buf)-1]     # remove '[', ']'

        return self.value


    def handle_int (self):

        idx = 0

        buf = ""
        
        while idx < len(self.value):

            c = self.value[idx]
            idx += 1

            if c == ',':
                break

            buf += c

        self.value = self.value[idx:len(self.value)]

        return int(buf)


    # get_next_item
    # - returns string for list 
    # - otherwise returns next integer

    def get_next_item (self):

        if len(self.value) == 0:
            return None

        idx = 0

        buf = ""

        if self.value[idx] == "[":     # list

            return self.handle_list()

        else:       # integer

            return self.handle_int()
              

# read lines from stdin
# populate lhs[], rhs[]

def get_input (lhs, rhs):

    num = 0
    
    for line in sys.stdin:
    
        line = line.rstrip()    # remove any white space from end of string
    
        if len(line) == 0:
            continue
    
        num += 1
        
        if num % 2 == 1:
            lhs.append(line)
        else:
            rhs.append(line)

    if len(lhs) != len(rhs):
        raise RuntimeError ("invalid input")


#
# main
# 

lhs = []
rhs = []

get_input (lhs, rhs)

num = 0

for i in range (len(lhs)):

    num += 1
    
    print ("pair#%d..." % (num))

    l = Expression(lhs[i])
    r = Expression(rhs[i])

    print (lhs[i])
    while True:
        ll = l.get_next_item()
        if not ll:
            break
        print ("ll=", ll)

    print ("")

    print (rhs[i])
    while True:
        rr = r.get_next_item()
        if not rr:
            break
        print ("rr=", rr)

    print ("")
