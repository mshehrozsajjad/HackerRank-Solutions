#!/bin/python

import sys


n = int(raw_input().strip())
def staircase(n):
    i,j=1,n-1
    while(i<=n):
        k=j
        while(k>0):
            sys.stdout.write(" "),
            k-=1
        k=1
        while(k<=i):
            sys.stdout.write("#"),
            k+=1
        sys.stdout.write("\n")
        j-=1
        i+=1
        
        
staircase(n)