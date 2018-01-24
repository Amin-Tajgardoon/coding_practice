# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:42:43 2018

Question: Given a binary tree, return one linkedlist per depth
@author: Amin
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.marked = False

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def dfs(root,h,arr):
    if len(arr) == h:
        ## arr is empty at index h
        arr.append(LinkedListNode(root.val))
    elif len(arr) > h:
        ## arr contains a linkedList at index h
        head = arr[h]
        while(head.next != None):
            head = head.next
        head.next = LinkedListNode(root.val)
    root.marked = True
    if root.left != None or root.right != None:
        ## dfs has not reached to a leaf, so increase depth
        h += 1
    if root.left != None and root.left.marked == False:
        ## unvisited node, so recurse
        dfs(root.left,h,arr)   
    if root.right != None and root.right.marked == False:
        ## unvisited node, so recurse
        dfs(root.right,h,arr)

if __name__ == '__main__':
    
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(10)    
    arr = []
    dfs(root, 0, arr)
    
    assert len(arr) == 3
    assert arr[0].val == 5
    assert arr[1].val == 3
    assert arr[1].next.val == 7
    assert arr[2].val == 1
    assert arr[2].next.val == 10
    
    