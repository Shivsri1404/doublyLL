#!/usr/bin/env python
# coding: utf-8

# In[22]:


class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None


# In[29]:


class DoublyLL:
    def __init__(self):
        self.head=None
        
    #insert in empty list
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Linked list is not empty")
            
    #insert start
    def insert_start(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            return
        new_node=Node(data)
        new_node.nref=self.head
        self.head.pref=new_node
        self.head=new_node
        
    #insert end
    def insert_end(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
            return
        n=self.head
        while n.nref is not None:
            n=n.nref
        new_node=Node(data)
        n.nref=new_node
        new_node.pref=n
    
    #insert after node
    def insert_after(self,data,x):
        if self.head is None:
            print("Linked List is empty")
            return
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.nref
        if n is None:
            print("item not in the list")
        else:
            new_node=Node(data)
            new_node.pref=n
            new_node.nref=n.nref
            if n.nref is not None:
                n.nref.pref=new_node
            n.nref=new_node
            
    #insert before node
    def insert_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")
            return
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.nref
        if n is None:
            print("item not in the list")
        else:
            new_node=Node(data)
            new_node.nref=n
            new_node.pref=n.pref
            if n.pref is not None:
                n.pref.nref=new_node
            n.pref=new_node
        
    
    
    #traverser_forward
    def traverse_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        n=self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n=n.nref
    #travers_backward
    def traverse_back(self):
        if self.head is None:
            print("Linked list is empty")
            return
        n=self.head
        while n.nref is not None:
            n=n.nref
        while n is not None:
            print(n.data,"-->",end=" ")
            n=n.pref


# In[30]:


DL=DoublyLL()
DL.traverse_forward()


# In[31]:


DL.insert_empty(10)
DL.traverse_forward()


# In[32]:


DL.insert_start(5)
DL.traverse_forward()


# In[33]:


DL.insert_end(15)
DL.traverse_forward()


# In[34]:


DL.insert_after(25,15)
DL.traverse_forward()


# In[35]:


DL.insert_before(20,25)
DL.traverse_forward()


# In[36]:


DL.traverse_back()


# In[ ]:




