#!/usr/bin/python3
#==========
# 32.py 
#==========

import sys

sum = 0
err = 0
num_lines = 0

brk = []

# list of sets
s = []
s.append(set())
s.append(set())
s.append(set())

for line in sys.stdin:

    lcl_line_num = num_lines % 3        # 0,1,2

    if lcl_line_num == 0:
        s[0].clear()
        s[1].clear()
        s[2].clear()


    num_lines += 1


    line = line.rstrip()

    for c in line:

        s[lcl_line_num].add(c)


    if lcl_line_num == 2:
        
        ss = s[0] & s[1] & s[2]

        if len(ss) > 1:

            print ("%s" % (str(ss)))
            err += 1
        else:

            sss = ""

            for cc in ss:
                sss += cc
                
            if sss.islower():
                sum += (ord(sss) - ord('a') + 1)

            elif sss.isupper():
                sum += (ord(sss) - ord('A') + 27)

            else:
                print ("not upper or lower")
                err +=1
           
            
print ("sum=%d, err=%d" % (sum,err))
        
