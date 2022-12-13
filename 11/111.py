#!/usr/bin/python3
#==========
# 111.py
#==========

import sys
import re

class Monkey:

    def __init__ (self, id):

        self.m_id           = id
        self.m_lst          = []
        self.m_op           = []
        self.m_tst          = []
        self.m_tst_true_mk  = None
        self.m_tst_false_mk = None

    def append_lst (self, lst):
        self.m_lst.append(lst)

    def set_op (self, op):
        self.m_op = op

    def set_tst (self, tst):
        self.m_tst = tst

    def set_tst_true_mk (self, tst_true_mk):
        self.m_tst_true_mk = tst_true_mk

    def set_tst_false_mk (self, tst_false_mk):
        self.m_tst_false_mk = tst_false_mk


#
# MAIN
#

# list of monkeys
monkeys = []

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    flds = line.split()

    if len(flds) == 0:
        print ("blank line skipped")
        continue

    if flds[0] == "Monkey":
        monkey_id = int(flds[1].replace(":",""))

        print ("monkey %d" % (monkey_id))

        m = Monkey(monkey_id)
        monkeys.append(m)

    else:
        print ("%s - Not Yet Handled" % (flds[0]))

