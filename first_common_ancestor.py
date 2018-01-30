# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:10:17 2018

@author: Amin
"""
from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def is_desc(root, node):
    if root == None:
        return False
    q = deque()
    q.append(root)
    while(len(q) > 0):
        n = q.popleft()
        if n == node:
            return True
        if n.left != None:
            q.append(n.left)
        if n.right != None:
            q.append(n.right)
        
def first_common_ances(root, n1, n2):
    if root == None:
        return None
    if is_desc(root, n1) and is_desc(root,n2):
        left = first_common_ances(root.left, n1, n2)
        right = first_common_ances(root.right, n1, n2)
        if left != None:
            return left
        if right != None:
            return right
        return root
        
if __name__=="__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(8)
    root.left.right = Node(4)
    root.left.right.left = Node(1)
    
    assert is_desc(root, root.left.right.left)
    assert not is_desc(root.right, root.left.right.left)
    
    assert first_common_ances(root, root.left.right, root.right) == root
    assert first_common_ances(root, root.left.right.left, root.left.right) == root.left.right