# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:00:25 2018

@author: Amin
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self):
        self.arr = [None]*100
    
    def insert(self, x):
        arr_indx = self.__hashfunc(x)
        if (self.arr[arr_indx] == None):
            self.arr[arr_indx] = Node(x)
        else:
            head = self.arr[arr_indx]
            cur = head
            while(cur.next != None):
                cur = cur.next
            cur.next = Node(x)
    
    def find(self, x):
        arr_indx = self.__hashfunc(x)
        if (self.arr[arr_indx] == None):
            return False
        cur = self.arr[arr_indx]
        while(cur!= None):
            if cur.val == x:
                return True
            cur = cur.next
        return False
        
    def __hashfunc(self,x):
        if x == None:
            raise TypeError("None value is not supported")
        return sum([ord(c) for c in x]) % 100
    
    def print_all(self):
        for i in range(0,len(self.arr)):
            if self.arr[i] == None:
                continue
            print('index=',i, sep='', end='->', flush=True)
            cur = self.arr[i]
            while(cur != None):
                print(cur.val, end='', flush=True)
                cur = cur.next
                if cur != None:
                    print(',', end='')
            print('')
    
    def remove(self, x):
        arr_indx = self.__hashfunc(x)
        if (self.arr[arr_indx] == None):
            return
        cur = self.arr[arr_indx]
        if cur.val == x:
            self.arr[arr_indx] = cur.next
            self.remove(x)
        while(cur.next!= None):
            if cur.next.val == x:
                cur.next = cur.next.next
                continue
            cur = cur.next
        

if __name__ == '__main__':
    ht = HashTable()
    ht.insert('AB')
    ht.insert('BC')
    ht.insert('ABC')
    ht.insert('AB')
    
    assert ht.find('AB')
    assert ht.find('ABC')
    assert not ht.find('EF')
    
    ht.remove('BC')
    assert not ht.find('BC')
    ht.remove('AB')
    assert not ht.find('AB')   