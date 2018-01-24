# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:28:49 2018

List of depth implementation with BFS

@author: Amin
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.marked = False

class LinkedListNode:
    def __init__(self):
        self.tree_node = None
        self.next = None
    
    def add(self, tree_node):
        cur = self
        if cur.tree_node == None:
            cur.tree_node = tree_node
            return
        while(cur.next != None):
            cur = cur.next
        cur.next = LinkedListNode()
        cur.next.tree_node = tree_node

def bfs(root):
    result = []
    cur = LinkedListNode()
    if root != None:
        cur.add(root)
    while(cur.tree_node != None):
        result.append(cur)
        parent = cur
        cur = LinkedListNode()
        while(parent != None):
            if parent.tree_node.left != None:
                cur.add(parent.tree_node.left)
            if parent.tree_node.right != None:
                cur.add(parent.tree_node.right)
            parent = parent.next
    return result
               

if __name__ == '__main__':
    
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(10)    
    arr = bfs(root)
    
    assert len(arr) == 3
    assert arr[0].tree_node.val == 5
    assert arr[1].tree_node.val == 3
    assert arr[1].next.tree_node.val == 7
    assert arr[2].tree_node.val == 1
    assert arr[2].next.tree_node.val == 10
