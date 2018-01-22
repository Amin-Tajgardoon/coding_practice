# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:38:13 2017

@author: Amin

input: two numbers in form of linkedlist where digits are sorted in reverse order
output: sum of two numbers as a linkedlist

"""

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(a, b):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """        
  #  a = l1
  #  b = l2
    head = ListNode(0)
    cur = head
    carry = 0
    while (a != None or b != None):
        a_val = a.val if a != None else 0
        b_val = b.val if b != None else 0
        s_tot = a_val + b_val + carry
        carry  = int(s_tot/10)
        cur.val = s_tot % 10
        if(a.next == None and b.next == None):
            break
        cur.next = ListNode(None)
        cur = cur.next
        a = a.next if a != None else None
        b = b.next if b != None else None
    
    
    if carry != 0:
        cur.next = ListNode(carry)
        
    return head

def toNum(l):
    i = 0
    num = 0
    while(l != None):
        num += l.val * (10**i)
        l = l.next
        i += 1
    return num
    
if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(6)
    
    result = addTwoNumbers(l,l)
    print(toNum(result))
    assert result.val == 2
    assert result.next.val == 4
    assert result.next.next.val == 2
    assert result.next.next.next.val == 1