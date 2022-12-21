#!/usr/bin/python3
#==========
# 131.py
#==========

import ch_list

import sys


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

answer = 0

# for each expression set

for i in range (len(lhs)):

    num += 1
    
    print ("pair#%d..." % (num))
    print ("lhs=%s" % (lhs[i]))
    print ("rhs=%s" % (rhs[i]))

    l = ch_list.List(lhs[i])
    r = ch_list.List(rhs[i])

    result = ch_list.compare_lists(l,r)

    print ("result=", result)
    print ("")

    if result == 1:
        answer += num

print ("answer:",answer)
