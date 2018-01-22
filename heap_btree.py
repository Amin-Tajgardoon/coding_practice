# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:07:45 2018

@author: Amin
"""
from collections import deque

class Heap:   
    def __init__(self, value):
        self.val = value
        self.parent = None
        self.left = None
        self.right = None
        
    def insert(self, val):
        new_node = Heap(val)
        q = deque()
        q.append(self)
        
        while(len(q) > 0):
            par = q.popleft()
            if par.left == None:
                par.left = new_node
                break
            if par.right == None:
                par.right = new_node
                break
            if par.left != None:
                q.append(par.left)
            if par.right != None:
                q.append(par.right)
        
        new_node.parent = par
        return new_node
        
    def pop(self):
        q = deque()
        q.append(self)
        
        while(len(q) > 0):
            node = q.popleft()
            if(node.left != None):
                q.append(node.left)
            if(node.right != None):
                q.append(node.right)
        
        par = node.parent
        if par.left != None and par.left.val == node.val:
            par.left = None
        else:
            par.right = None
        node.parent = None
        out = self.val        
        self.val = node.val
        return out
    
    def to_array_bfs(self):
        out = []
        self.__to_array_bfs(out)
        return out
                
    def __to_array_bfs(self, out):
        q = deque()
        q.append(self)
        
        while(len(q) > 0):
            par = q.popleft()
            out.append(par.val)
            if par.left != None:
                q.append(par.left)
            if par.right != None:
                q.append(par.right)

class MinHeap(Heap):    
    def __init__(self, value):
        super().__init__(value)

    def insert(self, val):
        new_node = super().insert(val)
        self.__bubble_up(new_node)
        
    def pop(self):
        out = super().pop()
        self.__bubble_down()
        return out
                
    def __bubble_up(self, node):        
        cur = node
        while(cur != None and cur.parent != None and cur.val < cur.parent.val):
            cur.parent.val = cur.val + cur.parent.val
            cur.val = cur.parent.val - cur.val
            cur.parent.val = cur.parent.val - cur.val
            cur = cur.parent
    
    def __bubble_down(self):
        cur = self
        while(cur != None):
            if cur.left != None and cur.right != None:
                child = cur.left if cur.left.val < cur.right.val else cur.right
            elif cur.left != None:
                child = cur.left
            else:
                break
            
            if child.val < cur.val:
                cur.val = cur.val + child.val
                child.val = cur.val - child.val
                cur.val = cur.val - child.val            
                cur = child
            else:
                break

class MaxHeap(Heap):    
    def __init__(self, value):
        super().__init__(value)

    def insert(self, val):
        new_node = super().insert(val)
        self.__bubble_up(new_node)
    
    def pop(self):
        out = super().pop()
        self.__bubble_down()
        return out
            
    def __bubble_up(self, node):        
        cur = node
        while(cur != None and cur.parent != None and cur.val > cur.parent.val):
            cur.parent.val = cur.val + cur.parent.val
            cur.val = cur.parent.val - cur.val
            cur.parent.val = cur.parent.val - cur.val            
            cur = cur.parent
            
    def __bubble_down(self):
        cur = self
        while(cur != None):
            if cur.left != None and cur.right != None:
                child = cur.left if cur.left.val > cur.right.val else cur.right
            elif cur.left != None:
                child = cur.left
            else:
                break
            
            if child.val > cur.val:
                cur.val = cur.val + child.val
                child.val = cur.val - child.val
                cur.val = cur.val - child.val            
                cur = child
            else:
                break


root = MinHeap(5)
root.insert(7)
root.insert(10)
root.insert(12)
root.insert(20)
root.insert(4)
root.insert(3)
arr = root.to_array_bfs()
assert arr == [3, 7, 4, 12, 20, 10, 5]


root = MaxHeap(5)
root.insert(7)
root.insert(10)
root.insert(12)
root.insert(20)
root.insert(30)
root.insert(40)
arr = root.to_array_bfs()
assert arr == [40, 12, 30, 5, 10, 7, 20]

root = MinHeap(5)
root.insert(7)
root.insert(10)
root.insert(12)
root.insert(20)
root.insert(4)
root.insert(3)
root.pop()
arr = root.to_array_bfs()
assert arr == [4, 7, 5, 12, 20, 10]


root = MaxHeap(5)
root.insert(7)
root.insert(10)
root.insert(12)
root.insert(20)
root.insert(30)
root.insert(40)
out = root.pop()
arr = root.to_array_bfs()
assert arr == [30, 12, 20, 5, 10, 7]