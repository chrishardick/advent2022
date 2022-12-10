#!/usr/bin/python3
#==========
# 92.py
#==========

import sys

def move_head (h, d):

    if d == "R":
        h[1] += 1

    elif d == "L":
        h[1] -= 1

    elif d == "U":
        h[0] += 1

    elif d == "D":
        h[0] -= 1

    else:
        raise RuntimeError ("move_head: Invalid Direction - %s" % (d))

#    if h[0] < 0:
#        raise RuntimeError ("move_head: Invalid y value")
#        
#    if h[1] < 0:
#        raise RuntimeError ("move_head: Invalid x value")


def move_tail (h, t, tt):
    
    if (h[0] == t[0] and h[1] == t[1]):
        pass

    elif h[0] == t[0] and abs(h[1]-t[1]) == 1:          # same row, adjacent
        pass

    elif h[1] == t[1] and abs(h[0]-t[0]) == 1:          # same col, adjacent
        pass

    elif abs(h[0]-t[0]) == 1 and abs(h[1]-t[1]) == 1:   # diagonal
        pass

    elif h[0] == t[0] and abs(h[1]-t[1]) == 2:          # same row, 2 apart
        if t[1] > h[1]:
            t[1] -= 1
        else:
            t[1] += 1

    elif h[1] == t[1] and abs(h[0]-t[0]) == 2:          # same col, 2 apart
        if t[0] > h[0]:
            t[0] -= 1
        else:
            t[0] += 1

    else: # move diagonal
        if t[0] < h[0]:
            t[0] += 1
        else:
            t[0] -= 1

        if t[1] < h[1]:
            t[1] += 1
        else:
            t[1] -= 1


#    else:
#        raise RuntimeError ("move_tail: Invalid Positions - h=%s, t=%s, tail#%d" % (h,t,tt+1))

#    if t[0] < 0:
#        raise RuntimeError ("move_tail: Invalid y value")
#        
#    if t[1] < 0:
#        raise RuntimeError ("move_tail: Invalid x value")


def update_tail_set (tail_set,t):

    key = "%s|%s" % (t[0], t[1])

    tail_set.add(key)
    


# head

h = [0,0]

# 9 tails

t = []

for tt in range(9):        # 0-8
    t.append([0,0])

t_set = set()

update_tail_set (t_set, t[8])


for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    l = line.split()            # [0] = [RLUD], [1] = #

    print ("%s" % (l))

    l[1] = int(l[1])

    print ("h=%s, t=%s" % (h,t))

    for hh in range (l[1]):
        
        move_head (h, l[0])

        for tt in range(9):
            if tt == 0:
                move_tail (h, t[0], tt)
            else:
                move_tail(t[tt-1],t[tt], tt)

        print ("h=%s. t=%s" % (h,t))

        update_tail_set(t_set,t[8])


print ("#=%d" % (len(t_set)))

