# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:13:15 2018

@author: Amin
"""

class MyQueue:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            
    def __init__(self):
        self.__first = None
        self.__last = None
        
    def add(self, val):
        if self.__last != None:
            self.__last.next = self.Node(val)
        self.__last = self.Node(val)
        if self.__first == None:
            self.__first = self.__last
            
    def pop(self):
        if self.__first == None:
            return None
        out = self.__first.val
        self.__first = self.__first.next
        if self.__first == None:
            self.__last = None
        return out
        
    def getFirst(self):
        if self.__first == None:
            return None
        return self.__first.val
    def getLast(self):
        if self.__last == None:
            return None
        return self.__last.val

    def isEmpty(self):
        return self.__first == None
    

if __name__ == '__main__':
    
    q = MyQueue()
    q.add(0)
    assert not q.isEmpty()
    assert q.getFirst() == 0
    assert q.getLast() == 0
    q.add(1)
    assert q.getFirst() == 0
    assert q.getLast() == 1
    q.add(2)
    assert q.getLast() == 2
    
    assert q.pop() == 0
    assert q.getFirst() == 1
    assert q.getLast() == 2
    q.pop()
    q.pop()
    assert q.isEmpty()
    assert q.pop() == None