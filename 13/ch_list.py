#!/usr/bin/python3
#==========
# ch_list.py
#==========

import collections

#
# List
#

class List:

    def __init__ (self,val):

        print ("List:", val)

        self.val = val

        if self.val[0] == '[':
            self.val = self.val[1:len(self.val)-1]

        self.entries = collections.deque()      # queue

        self._parse()


    def reset (self):

        self.entries.clear()
        self._parse()


    def __str__ (self):

        return "[" + str(self.val) + "]" 
        

    def next (self):

        if len(self.entries) == 0:
            print ("list=", self.val, "next=blank")
            return ""

        val = self.entries.popleft()
        print ("list=", self.val, "next=", val)
        return val


    # parse self.val
    # populate self.entries

    def _parse (self):

        idx = 0

        buf = ""

        stack = []

        while idx < len(self.val):

            c = self.val[idx]
            idx += 1

            if c == ',':
                if len(stack) == 0:

                    if buf.isdigit():
                        self.entries.append(int(buf))
                    else:
                        self.entries.append(buf)
                    buf = ""
                    continue

            buf += c

            if c == '[':
                stack.append(c)

            elif c == ']':
                stack.pop()

        if len(buf) != 0:
            if buf.isdigit():
                self.entries.append(int(buf))
            else:
                self.entries.append(buf)


#
# returns 
# - negative = less than
# - 0 = equal
# - positive = greater than
#
def compare_lists (l, r):

    print ("\ncompare_lists:",l,r,"...")

    l.reset()
    r.reset()

    while True:

        ll = l.next()
        rr = r.next()

        if isinstance(ll,str) and len(ll) == 0 and isinstance(rr,str) and len(rr) == 0:
            print ("ret=0")
            return 0

        if isinstance(ll,str) and len(ll) == 0 or isinstance(rr,str) and len(rr) == 0:

            # reached end of at least one list

            if isinstance(ll,str) and len(ll) == 0:
                print ("ret=-1")
                return -1       # ok (in order)

            print ("ret=1")
            return 1            # not ok (out of order)


        # if here, have yet to reach end of either list


        if isinstance(ll,str) or isinstance(rr,str):   # at least one list

            lll = List((str(ll)))
            rrr = List((str(rr)))

            ret = compare_lists(lll,rrr)

            if ret == 1 or ret == -1:
                print("ret=",ret)
                return ret

        else:       # both integers

            if ll < rr:         # ok (in order)
                print ("ret=-1")
                return -1

            elif ll > rr:
                print ("ret=1")
                return 1        # not ok (out of order)

    print ("ret=-1")
    return -1
