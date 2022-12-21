#!/usr/bin/python3
#==========
# 132.py
#==========

import ch_list

import sys

import functools

# read lines from stdin
# populate lhs[], rhs[]

def get_input (lst):

    for line in sys.stdin:
    
        line = line.rstrip()    # remove any white space from end of string
    
        if len(line) == 0:
            continue
  
        lst.append(ch_list.List(line))

    lst.append(ch_list.List("[[2]]"))
    lst.append(ch_list.List("[[6]]"))


#
# main
# 

lst = []

get_input (lst)

sorted_lst = sorted(lst, key=functools.cmp_to_key(ch_list.compare_lists))

print ("")
print ("results")

product = 1

idx = 0

for l in sorted_lst:

    idx += 1
    if str(l) == "[[6]]" or str(l) == "[[2]]":
        product *= idx
        print ("*",l)
    else:
        print (l)

print ("product:",product)


