#!/bin/python

import sys
def utopian(n):
    height=1
    for i in range(n+1):
        if(i>0):
            if(i%2==0):
                height+=1
            else:
                height = height*2
    return height


# n = int(raw_input().strip())
# d = raw_input().strip()
n= 4
result = utopian(n)
print result