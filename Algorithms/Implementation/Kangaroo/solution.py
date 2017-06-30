#!/bin/python

import sys


#There is no need to simulate the movement. We can reason that the 
#two kangaroos either meet at the smallest common multiply or never.

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if(x1==x2 and v1==v2):
        return 'YES'
    elif(x1==x2 and v1>v2):
        return 'NO'
    elif(x2>=x1 and v2>=v1):
        return 'NO'
    else:
        if (x2-x1)%(v1-v2)==0:
            return 'YES'
        else:
            return'NO'


x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)