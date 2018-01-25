# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 18:14:25 2018

Given a binary tree, determine whether it is imbalanced or not

@author: Amin
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.marked = False

#def height(root):
#    h=0
#    heights=[]
#    __height(root,h,heights)
#    print(heights)
#    return max(heights)

#def __height(root,h,heights):
#    
##    if root == None:
##        heights.append(h)
##        return
#    root.marked = True
#    if root.left == None and root.right == None:
#        heights.append(h)
#
#    if(root.left != None and root.left.marked == False):
#        root.left.marked = True
#        __height(root.left, h+1, heights)
#    if(root.right != None and root.right.marked == False):
#        root.right.marked = True
#        __height(root.right, h+1, heights)
        
def getHeight(root):
    if root == None:
        return -1
    return max([getHeight(root.left), getHeight(root.right)]) + 1

def is_balanced(root):
    if root == None:
        return True
    if root.left == None and root.right != None:
        return getHeight(root.right) <= 1
    if root.left != None and root.right == None:
        return getHeight(root.left) <= 1
    return is_balanced(root.left) and is_balanced(root.right)

if __name__=='__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.right.right = TreeNode(10)
    
    print(getHeight(root))
    assert is_balanced(root)
    
    root.left.left.left = TreeNode(7)
    root.left.left.left.left = TreeNode(7)
    root.left.left.left.left.left = TreeNode(7)
    print(getHeight(root))
    assert not is_balanced(root)
