#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()


# In[2]:


dir(iris)


# In[3]:


df=pd.DataFrame(iris.data,columns=iris.feature_names)


# In[4]:


df.head()


# In[5]:


df['target']=iris.target
df.head()


# In[6]:


df['flower_name']=df.target.apply(lambda x:iris.target_names[x])
df.head()


# In[7]:


x=df.drop(['target','flower_name'],axis='columns')
x.head()


# In[8]:


y=df['target']
y.head()


# In[9]:


from sklearn.model_selection inport train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[10]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[11]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


# In[12]:


len(x_train)


# In[13]:


len(x_test)


# In[14]:


from sklearn.svm import SVC
model=SVC(C=1)


# In[15]:


model.fit(x_train,y_trian)


# In[16]:


model.fit(x_train,y_train)


# In[17]:


model.score(x_test,y_test)


# In[18]:


y_predict=model.predict(x_test)


# In[19]:


from sklearn.metrics import classification_report
print(classification_report(y_test,y_predict))


# In[ ]:




