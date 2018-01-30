# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 22:23:28 2018

replace space with %20 in a string
input:
string, trueLength
output:
urlify of string

@author: Amin
"""

def urlify(s, l):
    s = list(s)
    cs = 0
    for i in range(l):
        if s[i] == ' ':
            cs += 1
    idx = l + cs*2
    for i in range(l-1,-1,-1):
        if s[i] == ' ':
            s[idx -1] = '0'
            s[idx -2] = '2'
            s[idx -3] = '%'
            idx -= 3
        else:
            s[idx-1] = s[i]
            idx -= 1
    return ''.join(s)
            
if __name__ == "__main__":
    s = "a b c       "
    s = urlify(s,6)
    assert s == "a%20b%20c%20"
        