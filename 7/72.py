#!/usr/bin/python3
#==========
# 72.py
#==========

import sys


path = []
hsh = {}

for line in sys.stdin:

    line = line.rstrip()        # remove any white space from end of string

    words = line.split()

    if words[0] == '$':         # a command

        if words[1] == 'cd':

            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])

                hkey = ""

                start = True

                for x in path:

                    hkey += x

                    if not start:
                        hkey += "/"
                    
                    start = False
                
                hsh[hkey] = 0

        elif words[1] == "ls":
            pass

    else:                       # ls results
        
        # directory listing

        if words[0] == "dir":
            pass

        else:

            # a file

            file_size = int(words[0])

            hkey = ""

            start = True

            for x in range(len(path)):

                hkey += path[x]

                if not start:
                    hkey += "/"

                start = False


                hsh[hkey] += file_size

total_size = 70000000
total_used = hsh["/"]

space_free = total_size - total_used
space_needed = 30000000 - space_free

print ("total:      %d" % (total_size))
print ("total used: %d" % (total_used))
print ("free:       %d" % (space_free))
print ("needed:     %d" % (space_needed))

l = []
for x in hsh:

    if hsh[x] >= space_needed:
        l.append (hsh[x])

l.sort()

print ("smallest:   %d" % (l[0]))
