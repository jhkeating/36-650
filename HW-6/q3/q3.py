#!/usr/bin/env python
# coding: utf-8

# In[37]:


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    # Print the linked list   
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            print("Deleted node is " + str(self.head.data))
            self.head = temp.next
            return

        while temp.next:
            if temp.next.data == data:
                print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return
    
    # Sort unsorted linked list in ascending order (modeled after selection sort)
    def sort(self):
        if not self.head: 
            return
        
        current_node = self.head
        
        # Traverse through all linked list nodes
        while (current_node):
            min_node = current_node
            next_node = current_node.next
            
            #  Find the minimum element in remaining unsorted linked list
            while (next_node):
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next
                
            # Swap the found minimum data value with the      
            start_val = current_node.data
            current_node.data = min_node.data
            min_node.data = start_val
            current_node = current_node.next
            


# In[39]:


# test case

first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(6)
linked_list.insert(2)
linked_list.insert(8)
linked_list.insert(4)
print("The Linked List is:")
linked_list.print_list()

linked_list.sort()
print("After sorting, the Linked List is:")
linked_list.print_list()

