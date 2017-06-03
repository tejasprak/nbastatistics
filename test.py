#!/usr/local/bin/python

import re


s = ['help', 'getstat']
command = "getstat hahahahaha"
cmdlen = len(command.split())
print cmdlen
i = 0
while i < 2:
    print command.split(' ', 1)[i]
    i = i  + 1

#print filter(lambda x: 'getstat' in x, command)
#print(filter((lambda x: re.search(r'getstat lol', x)),s))
