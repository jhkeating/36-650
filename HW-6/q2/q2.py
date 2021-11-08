#!/usr/bin/env python
# coding: utf-8

# In[37]:


class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        self.inner_list.insert(0, value)
        self.counter = self.counter + 1
        
    def dequeue(self):
        self.counter = self.counter - 1
        value = self.inner_list.pop(self.counter)
        return value
    
    def delete(self, value):
        # deletes all occurrences of value in self
        tmp = []
        while (self.counter!=0):
            tmp_val = self.dequeue()
            if (tmp_val != value):
                tmp.append(tmp_val)
        for val in tmp:
            self.enqueue(val)


# In[38]:


# test case

obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)
print(obj.inner_list)

obj.delete(7)
print(obj.inner_list)
print(obj.dequeue()) # should return 5

