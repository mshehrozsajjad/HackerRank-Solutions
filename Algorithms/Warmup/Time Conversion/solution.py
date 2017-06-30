#!/bin/python

import sys

def timeConversion(s):
    # Complete this function
    m = s[-2:] #The AM/PM part
    r = s[:-2] #Part without AM/PM i.e hh:mm:ss
    temp = int(s[:2]) #Hour Part i.e hh
    if(m == 'PM'):
        if (temp<12): #If in PM 01<=hh<=11 add 12
            temp = temp+12
        return str(temp)+r[2:] #Combining hh with mm:ss
    else:
        if(temp==12): #if in AM hh==12 then replace it with 00
            return '00'+r[2:]
        return r
    
    

#s = raw_input().strip()
s ="12:05:45AM"
result = timeConversion(s)
print(result)