# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 23:28:01 2018
Find inorder-successor for a given node in a BST

@author: Amin
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None

def inorder_traverse(root, node_val, last_seen_val, successor):
    if root == None:
        return
    inorder_traverse(root.left, node_val, last_seen_val, successor)
    if last_seen_val != None and last_seen_val == node_val and root.val > last_seen_val:
        successor.append(root.val)
        return
    last_seen_val = root.val
    inorder_traverse(root.right, node_val, last_seen_val, successor)
    
## NOT EFFICIENT: find root -> traverse tree from root -> return when successor reached    
def inorder_successor(node):
    if node == None:
        return None
    cur = node
    ## find root
    while(cur.parent != None):
        cur = cur.parent
    root = cur
    successor = []
    ## traverse from root until reach the successor
    inorder_traverse(root, node.val, None, successor)
    return None if len(successor)==0 else successor[0]


def smallest_on_left(node):
    if node == None:
        return None
    n = node
    while(n.left != None):
        n = n.left
    return n
    
## more efficient solution    
def inorder_Succ(node):
    if node == None:
        return None
    ## if node has right subtree, return the left most child
    if (node.right != None):
        return smallest_on_left(node.right)
    ## esle go up till the node is on the left side or None
    else:
        p = node.parent
        n = node
        while(p != None and p.left != n):
            n = p
            p = p.parent            
        return p
    
if __name__=="__main__":
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.parent = root
    root.right = TreeNode(8)
    root.right.parent = root
    root.right.left = TreeNode(7)
    root.right.left.parent = root.right
    root.right.right = TreeNode(10)
    root.right.right.parent = root.right
    root.left.right = TreeNode(4)
    root.left.right.parent = root.left
    root.left.right.left = TreeNode(3)
    root.left.right.left.parent = root.left.right
    
    #assert inorder_successor(root) == 7
    
    assert inorder_Succ(root).val == 7
    assert inorder_Succ(root.left.right).val == 5
    assert inorder_Succ(root.left).val == 3
    assert inorder_Succ(root.right.right) == None    
    
        
