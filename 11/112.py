#!/usr/bin/python3
#==========
# 112.py
#==========

import sys
import re
import math

class Monkey:

    def __init__ (self, id):

        self.m_id           = id
        self.m_lst          = []
        self.m_op           = []
        self.m_tst          = []
        self.m_true_target  = None
        self.m_false_target = None
        self.m_num_inspect  = 0

    def __str__ (self):

        if True:
            return "Monkey: id=%d,list_size=%d,insp=%d" % (self.m_id,len(self.m_lst),self.m_num_inspect)
        else:
            return "Monkey: id=%d,lst=%s,op=%s,tst=%s,true=%s,false=%s,insp=%d" % (
            self.m_id
            ,self.m_lst
            ,self.m_op
            ,self.m_tst
            ,self.m_true_target
            ,self.m_false_target
            ,self.m_num_inspect
            )

    def append_lst (self, lst):
        self.m_lst.append(lst)

    def set_op (self, op):
        self.m_op = op

    def set_tst (self, tst):
        self.m_tst = tst

    def set_true_target (self, tst_true_mk):
        self.m_true_target = tst_true_mk

    def set_false_target (self, tst_false_mk):
        self.m_false_target = tst_false_mk


#
# MAIN
#

dbg = False

# list of monkeys
monkeys = []

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    flds = line.split()

    if len(flds) == 0:
        dbg and  print ("blank line skipped")
        continue

    if flds[0] == "Monkey":
        monkey_id = int(flds[1].replace(":",""))

        dbg and print ("monkey %d" % (monkey_id))

        m = Monkey(monkey_id)
        monkeys.append(m)

    elif flds[0] == "Starting" and flds[1] == "items:":
    
        for x in range(2,len(flds)):
            item = int(flds[x].replace(",",""))
            monkeys[len(monkeys)-1].append_lst(item)

    elif flds[0] == "Operation:" and flds[1] == "new" and flds[2] == "=":

        monkeys[len(monkeys)-1].set_op(flds[3:len(flds)])
        
    elif flds[0] == "Test:" and flds[1] == "divisible" and flds[2] == "by":

        monkeys[len(monkeys)-1].set_tst(["%", flds[3]])

    elif (  flds[0] == "If" and 
            flds[1] == "true:" and 
            flds[2] == "throw" and 
            flds[3] == "to" and
            flds[4] == "monkey"):

        monkeys[len(monkeys)-1].set_true_target(int(flds[5]))

    elif (  flds[0] == "If" and 
            flds[1] == "false:" and 
            flds[2] == "throw" and 
            flds[3] == "to" and
            flds[4] == "monkey"):

        monkeys[len(monkeys)-1].set_false_target(int(flds[5]))

    else:
        print ("%s - Not Yet Handled" % (flds[0]))

for m in monkeys:
    print (m)

print ("")


for r in range(0,1000):

    if (r+1) % 10 == 0:
        print ("Round %d..." % (r+1))

        for m in monkeys:
            print (m)


    for m in monkeys:

        dbg and print (m)
    
        for ll in range (len(m.m_lst)):

            dbg and print ("ll=",ll)
            item = m.m_lst[ll]
   
            m.m_num_inspect += 1

            eval_str = ""
    
            for op in m.m_op:
    
                if op == "old": 
                    eval_str += str(item)
                else:
                    eval_str += str(op)
    
            dbg and print ("eval_str: ", eval_str)
    
            result = eval (eval_str)
    
            dbg and print ("result: ", result)
            
            if result % int(m.m_tst[1]) == 0:
                dbg and print ("True - target=%d" % (m.m_true_target))

                monkeys[m.m_true_target].m_lst.append(result)
            
            else:
                dbg and print ("False - target=%d" % (m.m_false_target))
                
                monkeys[m.m_false_target].m_lst.append(result)

        m.m_lst.clear()
            

dbg and print ("")

# product = 1

# tmp_lst = []

for m in monkeys:
    print (m)

#    tmp_lst.append(m.m_num_inspect)

# tmp_lst.sort(reverse=True)

# print ("product = %d" % (tmp_lst[0] * tmp_lst[1]))


