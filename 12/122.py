#!/usr/bin/python3
#==========
# 122.py
#==========


import sys
from collections import deque

dbg = False


class Solution:

    def __init__(self):

        self.lines              = []
        self.start              = None      # (y,x)
        self.end                = None      # (y,x)
        self.start_lst          = []        
        self.max_y              = None
        self.max_x              = None
    
    # given a tuple (y,x), return value at that location

    def get_value (self, tup):
        return lines[tup[0]][tup[1]]


    # load_matrix
    # - populate self.lines, max_y, max_x

    def load_matrix (self):

        for line in sys.stdin:
    
            line = line.rstrip()        # remove any white space from end of string

            self.lines.append(line)

        self.max_y = len(self.lines)-1
        self.max_x = len(self.lines[0])-1

        for l in self.lines:
            print ("|%s|" % (l))

        print ("")

        print ("max_y=", self.max_y)
        print ("max_x=", self.max_x)
        print ("")


    # find_start_and_end
    # - find starting and ending points. 
    # - populate self.start, self.end, self.start_lst

    def find_start_and_end (self):

        y = 0

        for line in self.lines:
    
            x = 0

            for c in line:
                if c == 'S':
                    self.start = (int(y),(int(x)))
                    self.start_lst.append((int(y),(int(x))))
                elif c == 'a':
                    self.start_lst.append((int(y),(int(x))))
                elif c == 'E':
                    self.end = (int(y),(int(x)))

                if self.start and self.end:
                    break

                x += 1
    
            y += 1
    
        if not self.start or not self.end:
            raise RuntimeError ("start or end not found")

        print ("start=%d,%d" % (self.start[0],self.start[1]))
        print ("end=%d,%d" % (self.end[0],self.end[1]))
        print ("start_lst=", self.start_lst, " size=", len(self.start_lst))

        print ("")


    # is_valid_step
    # - given current location (cur) and step location (stp)
    # - return boolean as to whether or not valid step

    def is_valid_step (self, cur, stp):

        cur_y = cur[0]
        cur_x = cur[1]

        cur_val = self.lines[cur_y][cur_x]

        if cur_val == 'S':
            cur_val = 'a'

        stp_y = stp[0]
        stp_x = stp[1]

        if stp_x < 0 or stp_x > self.max_x:
            return False

        if stp_y < 0 or stp_y > self.max_y:
            return False

        # if here, step is valid space

        stp_val = self.lines[stp_y][stp_x]
    
        if stp_val == 'E':
            stp_val = 'z'
        elif stp_val == 'S':
            stp_val = 'a'

        ret = False

        cur_ord = ord(cur_val)
        stp_ord = ord(stp_val)

        if stp_ord <= cur_ord+1:
            ret = True
        
        return ret


    # get_shortest_unvisited_node
    # - traverse list of unvisited nodes
    # - return the tuple (y,x) with shortest distance to start node

    def get_shortest_unvisited_node (self
                                    ,tbl            # [(y,x}] = { "shortest":, "prev": }
                                    ,unvisited
                                    ):

        min = None

        for u in unvisited:     # u = a tuple

            tbl_entry = tbl[u]

            if min == None:
                min = u
            else:
                if tbl_entry["shortest"] < tbl[min]["shortest"]:
                    min = u

        return min
    

    # dij
    # - find shortest path from start to end using Dijkstra's Shortest Path Algorithm

    def dij (self, start=None):

        unvisited   = set()
        visited     = set()

        tbl = {}

        node = { "shortest": 0, "prev": None }

        strt = None

        if start == None:
            strt = self.start
        else:
            strt = start

        print ("start=", strt)

        unvisited.add(strt)
        tbl[strt] = node

        distance = 0

        # 
        # load table
        #

        while (True):
            
            n = self.get_shortest_unvisited_node (tbl,unvisited)

            if n == None:
                break

            y = n[0]
            x = n[1]

            lst = []
            lst.append((y+1,x))
            lst.append((y-1,x))
            lst.append((y  ,x+1))
            lst.append((y  ,x-1))

            distance += 1

            for l in lst:
                if self.is_valid_step(n,l) and not l in visited:
                    unvisited.add(l)

                    if not l in tbl:
                        node = { "shortest": None, "prev": None }
                        tbl[l] = node

                    ll = tbl[l]

                    if ll["shortest"] == None or ll["shortest"] > distance:
                        ll["shortest"] = distance
                        ll["prev"] = n

            visited.add(n)
            unvisited.remove(n)
                       

        print ("table:")

        for t in tbl:
            print ("%s: %s" % (t, tbl[t]))

        print ("table done. #entries=", len(tbl))


        idx = self.end

        num_steps = 1

        while (True):
       
            if idx in tbl:
                entry = tbl[idx]
            else:
                return None         # path does not exist

            if entry["prev"] == strt:
                break

            idx = entry["prev"]
            num_steps += 1

        print ("num_steps=", num_steps, "\n")

        return num_steps
            


    # bfs
    # - find shortest path from S to E using bfs
    
    def bfs (self):

        visited = set()

        num_steps = 0

        q = deque()

        q.append((self.start,0))


        while len(q):

            cur = q.popleft()

            cur_pos         = cur[0]
            cur_num_steps   = cur[1]

            dbg and print ("y=%d,x=%d. #steps=%d" % (cur_pos[0],cur_pos[1], cur_num_steps))

            y = cur_pos[0]
            x = cur_pos[1]

            if self.lines[y][x] == 'E':
                print ("E found")
                return cur_num_steps


            visited.add(cur_pos)

            num_steps += 1

            if cur_num_steps % 10 == 0:
                print ("num_steps,",cur_num_steps)

            lst = []
            lst.append((y+1,x))
            lst.append((y-1,x))
            lst.append((y  ,x+1))
            lst.append((y  ,x-1))

            for l in lst:
                if l in visited:
                    dbg and print ("already visited", l)

                elif not self.is_valid_step(cur_pos, l):
                    dbg and print ("not a valid step", l)

                else:
                    dbg and print ("add to q", l)
                    q.append((l,cur_num_steps+1))

            dbg and print ("")

        raise RuntimeError ("E not found")


    def get_shortest_path_length (self):

        mnm = None

        num=0

        for i in self.start_lst:
            num += 1
            print ("iteration#", num)

            val = self.dij(i)

            if val:
                if mnm == None or val < mnm:
                    mnm = val;

        print ("minimum: ", mnm)

#
# main
#

s = Solution()

s.load_matrix()
s.find_start_and_end()

s.get_shortest_path_length()
