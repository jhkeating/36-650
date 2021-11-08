#!/usr/bin/env python
# coding: utf-8

# In[100]:


class Node:
    def __init__(self, data):
        self.tooBig = None # Too big child
        self.big = None # Big child
        self.small = None # Small child
        self.data = data # Node data

    def insert(self, data):
    # insert data into self tree
        if self.data:
            if data-self.data >= 10:
                if self.tooBig is None:
                    self.tooBig = Node(data)
                else: self.tooBig.insert(data)
                    
            elif data-self.data < 0:
                if self.small is None:
                    self.small = Node(data)
                else: self.small.insert(data)
                    
            else:
                if self.big is None:
                    self.big = Node(data)
                else: self.big.insert(data)
                    
        else: self.data = data
            
    def treeToList(self):
    # returns list of traversal of self 
    # small child -> root node -> big child -> tooBig child
        res = []
        if self:
            if self.small:
                 res = res + (self.small.treeToList())
            res.append(self.data)
            if self.big:
                 res = res + (self.big.treeToList())
            if self.tooBig:
                 res = res + (self.tooBig.treeToList())
        return res
    
    def delete(self, data):
    # delete data from self tree
        elements = self.treeToList()
        self.data = None
        self.small = None
        self.big = None
        self.tooBig = None
        for e in elements:
            if (e != data):
                self.insert(e)
            
    def traversal(self):
    # prints traversal of self (small child, root node, big child, tooBig child)
        if self.small:
             self.small.traversal()
        print(self.data)
        if self.big:
             self.big.traversal()
        if self.tooBig:
             self.tooBig.traversal()
    


# In[104]:


# test case

root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)
root.insert(50)
root.insert(65)
root.insert(45)

print("Tree contents after insertion using the traversal:")
root.traversal()

root.delete(45)

print("Tree contents after deleting 45 using traversal:")
root.traversal()

