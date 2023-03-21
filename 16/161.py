#!/usr/bin/python3
#==========
# 161.py
#
# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB 
#==========

import sys
import re

from valve import Valve


#
# Solution
#

class Solution:

    def __init__(self):
        self.dbg = False
        self.max_score = 0
        self.num_valves_with_flow_rate = 0
        self.num_open_valves = 0
        self.max_path = []

        self.valves = {}
        self.start = None       # Valve to start from


    def __str__(self):
        ss = 'Solution='
        ss += ' dbg=' + str(self.dbg)
        ss += ' max_score=' + str(self.max_score)
        ss += ' num_valves_with_flow_rate=' + str(self.num_valves_with_flow_rate)
        ss += ' num_open_valves=' + str(self.num_open_valves)
        ss += ' start=' + self.start.name

        ss += '\nvalves=\n'

        for v in self.valves:

            ss += str(self.valves[v]) + '\n'

        return ss


    # read input
    # - populate valves set, set starting valve, count # valves with flow rate

    def populate_valve_set (self):

        for line in sys.stdin:

            line = line.rstrip()        # remove any white space from end of string

            print (line)

            match = re.search ( r'Valve (.*?) has flow rate=(.*?); tunnels? leads? to valves? (.*$)'
                        ,line
                        )

            if not match:
                raise RuntimeError ("Invalid Line")

            name            = match.group(1)
            flow_rate       = int(match.group(2))
            valve_set_str   = match.group(3)

            self.valves[name] = Valve(name, flow_rate, valve_set_str)

            if not self.start:
                self.start = self.valves[name]

        for v in self.valves:
            if self.valves[v].flow_rate > 0:
                self.num_valves_with_flow_rate += 1

    
    # calculate costs to get from valve i to valve j 
    # where both valves have a flow rate

    def calc_costs (self):

        for i in self.valves:
            for j in self.valves:
                if i != j and (self.valves[i].flow_rate > 0 or self.valves[i]==self.start) and self.valves[j].flow_rate > 0:

                    c = self.find_shortest_path(self.valves[i], self.valves[j])

                    self.valves[i].add_cost(j,c)


    # return min # steps from Valve a to Valve b
    def find_shortest_path (self 
                            ,a          # Valve
                            ,b          # Valve
                            ):

        min_path = None

        path = []           # list of valve names
        path.append(a.name)

        visited = set()     # set of Valves
        visited.add(a)

        return self.dfs (a,b,min_path,path,visited)


    # dfs for shortest path from a to b
    
    def dfs (self
            ,a          # Valve
            ,b          # Valve
            ,min_path   # None or length
            ,path       # list of valve names
            ,visited    # set of Valves
            ):
    
        if a == b:

            # match found!
    
            l = len(path)-1
    
            if not min_path or l < min_path:
                min_path = l
    
            return min_path
    
    
        if min_path and len(path)-1 > min_path:
            return None
   

        for v in a.valve_list:
    
            if self.valves[v] not in visited:
                visited.add(self.valves[v])
                path.append(v)
    
                ret = self.dfs (self.valves[v], b, min_path, path, visited)
    
                if min_path:
                    if ret and ret < min_path:
                        min_path = ret
      
                elif ret:
                    min_path = ret
    
                path.pop()  # remove last item from list
                visited.remove(self.valves[v])
    
        return min_path

    
    #==========
    # get_top_score
    #==========

    def get_top_score (self):

        num_min = 0
        score = 0
        path = []

        self.dfs_top_score (self.start, num_min, score, path)

        return self.max_score


    # return
    # ======
    # max_score

    def dfs_top_score ( self
                        ,x                  # valve
                        ,num_min            # #min so far
                        ,score              # current score
                        ,path
                        ):
    
        if self.num_open_valves == self.num_valves_with_flow_rate:
            return

        if num_min >= 30:
            return

        path.append(x.name)

        if not x.open and x.flow_rate:
    
            # yet to open this valve and it has a flow rate
            # - open it
    
            x.open = True
    
            self.num_open_valves += 1
    
            num_min += 1
 
            if num_min == 30:
    
                x.open = False
                
                self.num_open_valves -= 1

                return
         
            score += x.flow_rate * (30-num_min)
    
            if score > self.max_score:
                self.max_score = score
                self.max_path = path
    
            if self.num_open_valves == self.num_valves_with_flow_rate:
                return
    
            for v in x.valve_cost:      # after open
    
                if num_min + x.valve_cost[v] > 30:
                    continue
    
                vv = self.valves[v]
    
                if vv.open == True:
                    continue
    
                num_min += x.valve_cost[v]
    
                self.dfs_top_score (vv  # Valve
                              ,num_min    # #min
                              ,score      # current score
                              ,path[:]
                              )
    
                num_min -= x.valve_cost[v]
   
            self.num_open_valves -= 1
    
            x.open = False
 

        for v in x.valve_cost:      # without open

            if num_min + x.valve_cost[v] > 30:
                continue

            vv = self.valves[v]

            if vv.open == True:
                continue

            num_min += x.valve_cost[v]

            self.dfs_top_score (vv  # Valve
                          ,num_min    # #min
                          ,score      # current score
                          ,path[:]
                          )

            num_min -= x.valve_cost[v]
   
        path.pop()

            
            

#
# main
#


solution = Solution()


# read input
# - populate valve set, set starting valve, count # of valves with flow rate

solution.populate_valve_set()

print ("\n")

# calculate min path to get from valve i to valve j
# - where both valves have a flow rate

solution.calc_costs()

print (solution)


solution.get_top_score()

print ("max_score=", solution.max_score)
print ("max_path=", solution.max_path)
