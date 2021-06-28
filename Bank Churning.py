#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv("C:/Users/Neethu Santhosh/Desktop/decoder lectures/case study/Bank_churn_modelling.csv")
df


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.info()


# In[7]:


df.head()


# In[8]:


df.columns


# In[9]:


cat=["Geography","Gender","HasCrCard","IsActiveMember","Exited"]
con=['CreditScore',"Tenure","Balance",'NumOfProducts',"EstimatedSalary","Age"]


# In[10]:


df=df.drop(['RowNumber', 'CustomerId', 'Surname'],axis=1)


# In[11]:


print(df.shape)
df.head()


# In[12]:


df.describe()


# In[13]:


df.isnull().sum()


# In[14]:


df["Geography"].unique()


# In[15]:


for i in cat:
    sns.countplot(x=i,data=df)
    plt.show()


# Analysis:- 
# 1. Almost 50% of customers are from France
# 2. 55% of bank customers are male and 45% are female
# 3. 70% of bank cutomers have credit card
# 4. Almost 50% of customers are not actively using bank services
# 5. 20% bank customers left the bank

# In[16]:


for i in con:
    sns.displot(df[i])
    plt.show()


# Analysis:-
# 1) Majority of bank customers have credit score between 400 to 850
# 2) Majority of customers have age in between 30 to 50
# 3) Majority of customers using 1 and 2 product of bank
# 4) There are two type of customer one who have bank balance 0 and other one whose bank balance between 50k to 200k

# In[17]:


#bivariate analysis
sns.countplot(x="Gender",hue="Exited",data=df)
plt.show()


# In[18]:


out=pd.crosstab(df["Gender"],df["Exited"],margins=True)
out


# In[19]:


out[1]/out["All"]


# In[20]:


sns.barplot(x="Gender",y="Exited",data=df)


# In[21]:


sns.barplot(x="Geography",y="Exited",data=df)
plt.show()


# In[22]:


cat


# In[23]:


sns.barplot(x="HasCrCard",y="Exited",data=df)
plt.show()


# In[24]:


sns.barplot(x='IsActiveMember',y="Exited",data=df)
plt.show()


# In[ ]:


Analysis:
1) Germany churing rate is high
2) churing rate is high for female
3) churing rate is small for customers who have CC 
4) churing rate is high for  customers who are not actively usng bank service


# In[25]:


sns.boxplot(x="Exited",y="CreditScore",data=df)
plt.show()


# In[27]:


sns.displot(df["CreditScore"][df["Exited"]==1],color='r')
sns.displot(df["CreditScore"][df["Exited"]==0],color='b')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




