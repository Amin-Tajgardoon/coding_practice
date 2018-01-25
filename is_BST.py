# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:13:59 2018

@author: Amin
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
def inorder_traverse(root, arr):
    if root == None:
        return
    inorder_traverse(root.left, arr)
    arr.append(root.val)
    inorder_traverse(root.right, arr)

## does not handle duplicates, O(N) memory space
def isBST_1(root):
    arr = []
    inorder_traverse(root, arr)
    print(arr)
    for i in range(len(arr)):
        j = min([i+1, len(arr)-1])
        if arr[i] > arr[j]:
            return False
    return True
    
## BEST O(N) handles duplicates
def __isBST(root, _min, _max):
    if root == None:
        return True
    if (_min != None and root.val <= _min) or (_max != None and root.val > _max):
        return False
    if (not __isBST(root.left, _min, root.val)) or (
    not __isBST(root.right, root.val, _max)):
        return False
    return True
    
def isBST(root):
    return __isBST(root, None, None)

## does not handle duplicates but O(1) spcae
def __isBST_2(root, last_printed):
    if root == None:
        return True
    
    if not __isBST_2(root.left, last_printed):
        return False
    
    if last_printed != None and root.val <= last_printed:
        return False
    last_printed = root.val
    
    if not __isBST_2(root.left, last_printed):
        return False
    
    return True

def isBST_2(root):
    return __isBST_2(root, None)

if __name__=='__main__':
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(1)
    
    assert not isBST(root)    
    assert not isBST_1(root)
    assert not isBST_2(root)