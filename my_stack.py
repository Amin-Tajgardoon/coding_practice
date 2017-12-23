# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 21:40:10 2017

@author: Amin
"""

class MyStack:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            
        def get_data(self):
            return self.data
            
        def set_next(self, next_node):
            self.next = next_node
            
        def get_next(self):
            return self.next
            
        def set_substack_min(self, substack_min):
            self.substack_min = substack_min
            
        def get_substack_min(self):
            return self.substack_min

    def __init__(self):
        self.top = None
        self.min = None
        
    def peek(self):
        return self.top.get_data()
        
    def push(self, data):
        newNode = self.StackNode(data)
        if self.min == None:
            self.min = data
        else:
            self.min = data if data < self.min else self.min
        newNode.set_substack_min(self.min)
            
        if self.top == None:
            self.top = newNode
        else:
            newNode.set_next(self.top)
            self.top = newNode
    
    def pop(self):
        if self.top == None:
            raise Exception('empty stack!')
        t = self.top
        self.top = t.get_next()
        self.min = self.top.get_substack_min() 
        return t.get_data()
        
    def get_min(self):
        return self.min            
                
if __name__=="__main__":
    s1 = MyStack()
    s1.push(1)
    s1.push(3)
    assert s1.get_min() == 1
    s1.push(5)
    s1.push(0)
    assert s1.get_min() == 0
    p = s1.pop()
    assert p == 0
    assert s1.get_min() == 1