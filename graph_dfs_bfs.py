# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:33:31 2018

@author: Amin
"""
from collections import deque

class Graph:
    def __init__(self):
        self.nodes = []
    
    def add(self, node):
        self.nodes.append(node)
    def add_all(self, node_list):
        self.nodes = self.nodes + node_list
    def reset_marked(self):
        for n in self.nodes:
            n.marked = False
    
    def __DFS(self, root, output):
        if root == None:
            return
        output.append(root.val)
        root.marked = True
        for node in root.adjacency_list:
            if node.marked == False:
                self.__DFS(node, output)

    def DFS(self, root):
        output = []
        self.reset_marked()
        self.__DFS(root, output)
        self.reset_marked()
        return output
        
    def __BFS(self, root, output):
        if root == None:
            return
        q = deque()
        q.append(root)
        while(len(q) > 0):
            node = q.popleft()
            output.append(node.val)
            node.marked = True
            for adj in node.adjacency_list:
                if adj.marked == False:
                    q.append(adj)
    
    def BFS(self, root):
        output = []
        self.reset_marked()
        self.__BFS(root, output)
        self.reset_marked()
        return output

class Node:
    def __init__(self, val):
        self.val = val
        self.marked = False
        self.adjacency_list = []

if __name__ == '__main__':
    
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n0.adjacency_list = [n1, n4, n5]
    n1.adjacency_list = [n3, n4]
    n2.adjacency_list = [n1]
    n3.adjacency_list = [n2, n4]
    n4.adjacency_list = []
    n5.adjacency_list = []    

    g= Graph()
    g.add_all([n0,n1,n2,n3,n4,n5])

    assert g.DFS(n0) == [0,1,3,2,4,5]
    assert g.DFS(n0) == [0,1,3,2,4,5]
    assert g.BFS(n0) == [0,1,4,5,3,4,2]
    assert g.BFS(n0) == [0,1,4,5,3,4,2]