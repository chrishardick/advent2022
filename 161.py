#!/usr/bin/python3
#==========
# 161.py
#
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB 
#==========

import sys
import re

from valve import Valve


max_score = 0

#
# return
# (num_min, open_valve_sum, max_score)
#
def dfs_top_score ( x                   # valve
                    ,valves             # Valve set
                    ,num_min            # #min so far
                    ,score              # current score
                    ,open_valve_sum
                    ):

    global max_score

    print ("\nMIN=", num_min
            ," AT valve=", x.name
            ," SCORE=", score
            ," open_valve_sum=", open_valve_sum
            ," max_score", max_score
            ," dfs_top_score TOP"
            )

    if score > max_score:
        max_score = score
        print ("NEW MAX_SCORE=",max_score, " TOP")

    if num_min >= 30:
        print ("returning from valve ", x.name, " num_min=", num_min, " max_score=", max_score)
        return (num_min, open_valve_sum, max_score)

    # if here, num_min <= 29

    lcl_num_min = 0
    lcl_open_valve_sum = 0
    lcl_max_score = 0

    sav_score           = score
    sav_num_min         = num_min
    sav_open_valve_sum  = open_valve_sum

    if not x.open and x.flow_rate:

        # yet to open this valve and it has a flow rate
        # - open it

        x.open = True

        num_min += 1

        score += open_valve_sum

        open_valve_sum += x.flow_rate       # 1 minute

        print ("\nMIN=", num_min
                ," OPEN VALVE [", x.name, " flow rate", x.flow_rate , "]"
                ," SCORE=", score
                ," open_valve_sum=", open_valve_sum
                ," max_score=", max_score
                )

        if score > max_score:
            max_score = score
            print ("NEW MAX_SCORE=",max_score, " open valve")

        if num_min >= 30:
            print ("returning after opening value", x.name)
            return (num_min, open_valve_sum, max_score)
      

        for v in x.valve_cost:

            if num_min + x.valve_cost[v] > 30:
                continue

            vv = valves[v]

            new_score = score + (open_valve_sum*x.valve_cost[v])

            print ("cost to get to valve ", vv.name, " ", x.valve_cost[v])

            (lcl_num_min, lcl_open_valve_sum, lcl_max_score) = dfs_top_score (vv  # Valve
                                    ,valves                         # Valve set
                                    ,num_min+x.valve_cost[v]        # #min
                                    ,new_score                      # current score
                                    ,open_valve_sum                 # open valve sum
                                    )

        while lcl_num_min < 30:
            print ("another minute")
            lcl_max_score += lcl_open_valve_sum
            lcl_num_min += 1

        if lcl_max_score > max_score:
            max_score = lcl_max_score
            print ("NEW MAX_SCORE=",max_score, " after open traversal")


        x.open = False


    # handle the 'do not open' the valve case

    print ("valve", x.name, " handle 'do not open' case")

    score           = sav_score
    num_min         = sav_num_min
    open_valve_sum  = sav_open_valve_sum

    for v in x.valve_cost:

        if num_min + x.valve_cost[v] > 30:
            print ("valve=", x.name, " num_min=", num_min, " cannot get to valve ", v, " cost=", x.valve_cost[v])
            continue

        vv = valves[v]

        new_score = score + (open_valve_sum*x.valve_cost[v])

        print ("cost to get to valve ", vv.name, " ", x.valve_cost[v])

        (lcl_num_min, lcl_open_valve_sum, lcl_max_score) = dfs_top_score (vv    # Valve
                                                    ,valves                     # Valve set
                                                    ,num_min+x.valve_cost[v]    # #min
                                                    ,new_score                  # current score
                                                    ,open_valve_sum             # open valve sum
                                                    )   

    while lcl_num_min < 30:
        print ("num_min=", lcl_num_min, " another minute")
        lcl_max_score += lcl_open_valve_sum
        lcl_num_min += 1

    if lcl_max_score > max_score:
        max_score = lcl_max_score
        print ("NEW MAX_SCORE=",max_score, " after do not open traversal")

    print ("RETURNING FROM VALVE ", x.name)
    return (lcl_num_min,lcl_open_valve_sum,max_score)      # #min,open_valve_sum,max

            
    
def get_top_score ( start       # Valve
                    ,valves
                    ):

    global max_score

    num_min = 0
    score = 0
    open_valve_sum = 0
   
    (lcl_num_min, lcl_open_valve_sum, lcl_max_score) = dfs_top_score (start
                                                                    ,valves
                                                                    ,num_min
                                                                    ,score
                                                                    ,open_valve_sum
                                                                    )

    return max_score



# dfs for shortest path

def dfs (a          # Valve
        ,b          # Valve
        ,valves     # set of Valves
        ,min_path   # None or length
        ,path       # list of valve names
        ,visited    # set of Valves
        ):

    minp = None

    if a == b:
        # print ("match found! path=", path)

        l = len(path)-1

        if not min_path or l < min_path:
            min_path = l

        return min_path


    if min_path and len(path)-1 > min_path:
        return None

    for v in a.valve_list:

        if valves[v] not in visited:
            visited.add(valves[v])
            path.append(v)

            ret = dfs (valves[v], b, valves, min_path, path, visited)

            if minp:
                if ret and ret < minp:
                    minp = ret
  
            elif ret:
                minp = ret

            path.pop()  # remove last item from list
            visited.remove(valves[v])

    return minp
    
    
# return min # steps from Valve a to Valve b
def find_shortest_path (a           # Valve
                        ,b          # Valve
                        ,valves     # set of Valves
                        ):

    min_path = None

    path = []           # list of valve names
    path.append(a.name)

    visited = set()     # set of Valves
    visited.add(a)

    return dfs (a,b,valves,min_path,path,visited)
    

#
# main
#


valves = {} # Valve map. key = valve name


start = None

# read input, populate valves

print ("Reading input, constructing Valve map...")

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    print (line)

    match = re.search ( r'Valve (.*?) has flow rate=(.*?); tunnels? leads? to valves? (.*$)'
                        ,line
                        )

    if not match:
        raise RuntimeError ("Invalid Line")

    valve_name      = match.group(1)
    flow_rate       = int(match.group(2))
    valve_set_str   = match.group(3)

    valves[valve_name] = Valve(valve_name, flow_rate, valve_set_str)

    if not start:
        start = valves[valve_name]
        print ("start=",start)


print ("Done Reading Input\n")


#print ("Valves (before calculating costs)...")
#
#for v in sorted(valves):
#    print (valves[v])
#
#print ("Done printing Valves\n")


#print ("Calculating costs...");
#
for i in sorted(valves):

    for j in sorted(valves):
        if i != j and (valves[i].flow_rate > 0 or valves[i]==start) and valves[j].flow_rate > 0:
            c = find_shortest_path(valves[i], valves[j], valves)

            valves[i].add_cost(j,c)

#print ("Done calculating costs\n")


print ("Valves (after calculating costs)...")

for v in sorted(valves):
    print (valves[v])

print ("Done printing valves\n")


#
# now we want to do a dfs to find the best score...
#

print ("calculate top score...")

top_score = get_top_score (start, valves)

print ("top score = ", top_score)
