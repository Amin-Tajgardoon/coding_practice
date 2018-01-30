# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 23:13:26 2018

@author: Amin
"""

def is_perm_palind(s):
    
    t = [0]*(ord('z')-ord('a')+1)
    for c in s:
        if c == ' ':
            continue
        t[ord('z')-ord(c.lower())] +=1
    count_odd = 0    
    for i in t:
        if i % 2 != 0:
            count_odd += 1
    return count_odd <= 1
    
if __name__=="__main__":
    s = "Tact coa"
    assert is_perm_palind(s)
    assert not is_perm_palind("Tact ccoa")