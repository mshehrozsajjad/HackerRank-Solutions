#!/bin/python

import sys

def sherlockAndAnagrams(iterable):
    # Complete this function
    subsets =[]
    s = tuple(iterable)
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            subsets.append(iterable[index:index+size])
    
    test = []
    match=0
    blacklist=[]

    for substring in subsets:
        test.append(''.join(sorted(substring)))
    final_sorted =  sorted(test)

    for i in range(len(final_sorted)):
        for j in range(i+1, len(final_sorted)):
            if final_sorted[i] == final_sorted[j]:
                match  += 1
                
    return match

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = sherlockAndAnagrams(s)
    print(result)