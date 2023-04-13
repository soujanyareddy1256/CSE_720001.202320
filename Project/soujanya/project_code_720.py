#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing essential libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Importing the necessary data and loading the data

# In[2]:


# Loading the dataset
df = pd.read_csv('admission_predict.csv')


# # Exploring the dataset

# In[3]:


# Returns number of rows and columns of the dataset
df.shape


# In[4]:


# Returns the first x number of rows when head(num). Without a number it returns 5
df.head()


# In[5]:


# Returns the first x number of rows when tail(num). Without a number it returns 5
df.tail()


# In[6]:


# Returns an object with all of the column headers
df.columns


# In[7]:


# Returns basic information on all columns
df.info()


# # Performing Calculations

# In[8]:


# Returns basic statistics on numeric columns
df.describe().T


# In[ ]:




