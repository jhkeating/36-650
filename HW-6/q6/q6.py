#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None

# Class to create a  Reverse Linked List
class ReverseLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail
        
    def print_list(self):
        # Print the reverse linked list
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n") 
        
    def insert(self, data):
        # Insert a node in a reverse linked list
        node = Node(data)
        if not self.tail:
            self.tail = node
        else:
            temp = self.tail
            self.tail = node
            self.tail.previous = temp
            
    def delete(self, data):
        # Delete a node in a reverse linked list
        if not self.tail:
            return 

        temp = self.tail

        # Check if tail node is to be deleted
        if self.tail.data == data:
            print("Deleted node is " + str(self.tail.data))
            self.tail = temp.previous
            return

        while temp.previous:
            if temp.previous.data == data:
                print("Node deleted is " + str(temp.previous.data))
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        print("Node not found")
        return
    
    def search(self, data):
        # Returns true/false based on if data is stored in nodes of self
        if not self.tail:
            return False
        
        current = self.tail
        while current:
            if current.data == data:
                return True
            current = current.previous
        return False


# In[14]:


# test case

first_node = Node(11)
linked_list = ReverseLinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

print("After insertion, the Reverse Linked List is:")
linked_list.print_list()

linked_list.delete(6)

print("After deleting 6, the Reverse Linked List is:")
linked_list.print_list()

print("Does 5 exist in the Reverse Linked List?")
print(linked_list.search(5))

print("Does 17 exist in the Reverse Linked List?")
print(linked_list.search(17))

