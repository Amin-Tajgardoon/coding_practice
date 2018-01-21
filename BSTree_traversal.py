# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:45:23 2018

@author: Amin
"""

class TreeNode:
    
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def visit(tree_node):
    if tree_node != None:
        return (tree_node.val)

def in_order(node, result):
    if node != None:
        in_order(node.left, result)
        result.append(visit(node))
        in_order(node.right, result)

def pre_order(node, result):
    if node != None:
        result.append(visit(node))
        in_order(node.left, result)
        in_order(node.right, result)

def post_order(node, result):
    if node != None:
        in_order(node.left, result)
        in_order(node.right, result)
        result.append(visit(node))
        

node = TreeNode(2)
node.left = TreeNode(1)
node.right = TreeNode(3)

arr= []
in_order(node, arr)
assert arr == [1,2,3]

arr= []
pre_order(node, arr)
assert arr == [2,1,3]

arr= []
post_order(node, arr)
assert arr == [1,3,2]
