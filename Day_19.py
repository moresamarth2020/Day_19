#!/usr/bin/env python
# coding: utf-8

# # Python Tuples
# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

# In[4]:


tup = (1,2,3,4)
print(type(tup),tup)


# In[5]:


tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)


# In[6]:


details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)


# ## Tuple Indexes
# Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.

# In[7]:


country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]              


# ### Accessing tuple items:
# ##### 1. Positive Indexing:
# As we have seen that tuple items have index, as such we can access items using these indexes.
# - Example:

# In[8]:


country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]     
print(country[0])
print(country[1])
print(country[2])


# In[11]:


Num = (10,15,20,25,30,35,40)
print(Num[0])
print(Num[1])
print(Num[2])
print(Num[3])
print(Num[4])


# #### II. Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

# In[12]:


country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])


# In[13]:


print(country[len(country)-1])


# In[28]:


Num = (10,15,20,25,30,35,40,45)
print(Num[len(Num)-1])
print(Num[-1])
print(Num[-7])
print(Num[-6])
print(Num[-5])
print(Num[-4])
print(Num[-3])
print(Num[-2])
print(Num[-1])
print(Num[0])


# #### 3. Check for item:
# We can check if a given item is present in the tuple. This is done using the in keyword.

# In[29]:


country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")


# In[32]:


Num = (10,15,20,25,30,35,40)
if 15 in Num:
    print("15 is Present")
else:
    print("15 is Not Present")


# In[36]:


country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")


# #### Example: Printing elements within a particular range:
# Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values. Note: The element of the end index provided will not be included.

# In[40]:


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes


# #### Example: Printing all element from a given index till the end
# When no end index is provided, the interpreter prints all the values till the end.

# In[41]:


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes


# #### Example: printing all elements from start to a given index
# When no start index is provided, the interpreter prints all the values from start up to the end index provided.

# In[44]:


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes


# ### Example: Print alternate values
# Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.

# In[46]:


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes


# #### Example: printing every 3rd consecutive withing given range

# In[49]:


animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])


# Here, jump index is 3. Hence it prints every 3rd element within given index.

# In[ ]:




