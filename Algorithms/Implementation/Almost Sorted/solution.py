#!/bin/python
def orderIt(d,n):
    #Getting Numbers List
    result = 'no'
    lst=[]
    for word in d.split(' '):
        lst.append(int(word))
    
    missed=[]
    match=0
    #Check if already sorted
    for i in range(0,n-1):
        if(lst[i+1])>=(lst[i]):
            match+=1
        else:
            missed.append(i)

    if(match==n-1):
        return 'yes'
    

    #Check swap
    
    if(len(missed)==1):
        l,r = missed[0],missed[0]+1
    else:
        l,r  = missed[0],missed[1]+1

    tlist=list(lst)
    temp = tlist[l]
    tlist[l] = tlist[r]
    tlist[r] = temp
    match=0
    nmissed=[]

    for i in range(0,n-1):
        if(tlist[i+1])>=(tlist[i]):
            match+=1
        else:
            nmissed.append(i)
    if(match==n-1):
        return 'yes\nswap '+str(l+1)+' '+str(r+1)

    #Check Reverse
    
    l,r = missed[0],missed[-1:]
    r = int(r[0])+1
    tlist= list(lst)
    tcount = 0
    for i in range(n):
        if(i>=l and i<r-tcount):
            temp = tlist[i]
            tlist[i] = tlist[r - tcount]
            tlist[r - tcount] = temp
            tcount+=1

    match=0
    missed=[]

    for i in range(0,n-1):
        if(tlist[i+1])>=(tlist[i]):
            match+=1
        else:
            missed.append(i)
    if(match==n-1):
        return 'yes\nreverse '+str(l+1)+' '+str(r+1)
    else:
        return'no'


# n = int(raw_input().strip())
# d = raw_input().strip()
n= 10
d= '1 2 3 4 6 5 7 8 9 10'
result = orderIt(d,n)
print result