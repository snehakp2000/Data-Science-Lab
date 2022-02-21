#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


from sklearn import datasets
wine=datasets.load_wine()
print(wine)


# In[3]:


from sklearn import datasets
wine=datasets.load_wine()
print(wine)


# In[4]:


print(wine.feature_names)


# In[5]:


print(wine.target_names)


# In[6]:


x=pd.DtaFrame(wine['data'])
print(x.head())


# In[8]:


x=pd.DataFrame(wine['data'])
print(x.head())


# In[9]:


from sklearn.naive_bayes import GaussianGB
gnb=GaussianNB()
gnb.fit(x_train,y_train)
y_ppred=gnb.predict(x_test)
print(y_pred)


# In[10]:


from sklearn.naive_bayes import GaussianGB
gnb=GaussianNB()
gnb.fit(x_train,y_train)
y_pred=gnb.predict(x_test)
print(y_pred)


# In[11]:


from sklearn.naive_bayes import GaussianNB


# In[12]:


gnb=GaussianNB()
gnb.fit(x_train,y_train)
y_pred=gnb.predict(x_test)
print(y_pred)


# In[ ]:




