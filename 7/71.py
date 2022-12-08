#!/usr/bin/python3
#==========
# 71.py
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

            continue

    else:
        
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


total = 0

for x in hsh:

    if hsh[x] <= 100000:
        total += hsh[x]

    print ("%s %d %s" % (x, hsh[x], s))

print ("total=%d" % (total))
