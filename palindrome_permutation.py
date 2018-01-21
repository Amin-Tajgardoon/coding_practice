# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:49:46 2018

@author: Amin
"""

def isPalindromePerm(s):
    s = s.replace(' ','')
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    if len(s) % 2 == 0:
        for _,v in d.items():
            if v%2 == 1:
                return False
    else:
        count_ones = 0
        for _,v in d.items():
            if v % 2 == 1 and v != 1:
                return False
            elif v == 1:
                count_ones +=1
                if count_ones != 1:
                    return False
        
    return True
    
    
assert isPalindromePerm('aba b')
assert not isPalindromePerm('aba bb')
assert isPalindromePerm('aba')
assert isPalindromePerm('aa b')
assert not isPalindromePerm('aa bccc ')