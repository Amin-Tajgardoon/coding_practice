# -*- coding: utf-8 -*-
"""
Q: create a binary search tree with minimal height from a sorted array of 
unique integeres (increasing order).

Created on Wed Jan 24 11:55:50 2018

@author: Amin
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.marked = False

def toBST(arr):
    if len(arr) == 0:
        return
    m_idx = int(len(arr)/2)
    root = Node(arr[m_idx])
    root.left = None if m_idx == 0 else toBST(arr[0:m_idx])
    root.right = None if m_idx == 0 else toBST(arr[m_idx+1:])
    return root

def dfs(root,h,max_h):
    root.marked = True
    if root.left != None or root.right != None:
        h += 1
    else:
        max_h.append(h)
    if root.left != None and root.left.marked == False:
        dfs(root.left,h,max_h)
    
    if root.right != None and root.right.marked == False:
        dfs(root.right,h,max_h)

def add(root, val):
    cur = root
    while(cur != None):
        if val > cur.val:
            if cur.right == None:
                cur.right = Node(val)
                return
            cur = cur.right
        else:
            if cur.left == None:
                cur.left = Node(val)
                return
            cur = cur.left
                            
if __name__ == '__main__':
    arr = list(range(5))
    root = toBST(arr)
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 4
    assert root.right.left.val == 3
    assert root.left.left.val == 0
    
    ## test of height
    max_h = []
    dfs(root,1,max_h)
    assert max(max_h) == 3
    
    ## test for insert to a BST, not related to the main problem 
    root = Node(5)
    for i in range(10):
        add(root, i)
    max_h = []
    dfs(root,1,max_h)
    assert max(max_h) == 7