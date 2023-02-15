#!/usr/bin/python3
#==========
# valve.py
#==========

class Valve:

    def __init__(self, name, flow_rate, valve_set_string):

        self.name = name
        self.flow_rate = flow_rate

        self.open = False

        valve_set_string = valve_set_string.replace (",", "")              # remove commas

        self.valve_list = valve_set_string.split()      # split on spaces

        self.valve_cost = {}     # ["name"] => cost to get to "name" - i.e. # minutes


    def add_cost (self,dest,cost):

        self.valve_cost[dest] = cost

    def __str__(self):

        return  ("name=%s, flow_rate=%d, open=%s, valve_list=%s, cost_map=%s" %
                (self.name
                ,self.flow_rate
                ,self.open
                ,self.valve_list
                ,self.valve_cost
                ))

    def __lt__(self,other):
        return self.name < other.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self,other):
        return (self.name == other.name)
        
