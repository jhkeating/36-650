#!/usr/bin/env python
# coding: utf-8

# In[4]:


# removes keys in list l from dictionary d
def delete_keys(l, d):
     for key in l:
        # check that key exists in dictionary before removing
        if key in d:
            d.pop(key)
        return d


# In[5]:


# test case

d = {"firstName":"Mohamed", "lastName":"Farag", "birthYear":1990, "nationality":"Egyptian"}
print(delete_keys(["lastName","birthYear","favoriteColor"], d))

