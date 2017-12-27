# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:38:13 2017

@author: Amin
"""

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """        
    a = l1
    b = l2
    temp_head = ListNode(0)
    cur = temp_head
    carry = 0
    while (a != None or b != None):
        a_val = a.val if a != None else 0
        b_val = b.val if b != None else 0
        s_tot = a_val + b_val + carry
        carry  = int(s_tot/10)
        cur.next = ListNode(s_tot % 10)
        cur = cur.next
        a = a.next if a != None else a
        b = b.next if b != None else b
        
    if carry != 0:
        cur.next = ListNode(carry)
        
    return temp_head.next
    
if __name__ == '__main__':
    