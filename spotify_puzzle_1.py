
# coding: utf-8

# In[32]:


x = 47
bin(x)


# In[33]:


str_x = str(bin(x))


# In[34]:


reverse_x = str_x[::-1]


# In[35]:


ans_bin = reverse_x[:len(reverse_x)-2]


# In[37]:


int(ans_bin,2)

