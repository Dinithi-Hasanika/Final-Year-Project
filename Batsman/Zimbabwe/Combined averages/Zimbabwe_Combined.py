#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#load data file
data = pd.read_csv('C:/Users/HP/Desktop/Zimbabwe.csv')


# In[3]:


data.head()


# In[4]:


x = set()


# In[5]:


players = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11']
player_scores = ['p1-s','p2-s','p3-s','p4-s','p5-s','p6-s','p7-s','p8-s','p9-s','p10-s','p11-s']


# In[6]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[7]:


print(x)
len(x)


# In[8]:


import itertools 
# def findsubsets(s, n): 
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 


# In[9]:


# print(findsubsets(x,2))


# In[10]:


len(findsubsets(x,2))


# In[11]:


# print(findsubsets(x,3))


# In[12]:


len(findsubsets(x,3))


# In[13]:


# print(findsubsets(x,4))


# In[14]:


len(findsubsets(x,4))


# In[15]:


len(findsubsets(x,5))


# In[16]:


# sub = findsubsets(x,2)
# sub = findsubsets(x,3)
sub = findsubsets(x,4)


# In[17]:


# column_names = ["player-1", "player-2", "avg"]
# column_names = ["player-1", "player-2","player-3", "avg"]
column_names = ["player-1", "player-2","player-3","player-4", "avg"]

result_grams = pd.DataFrame(columns = column_names)


# In[18]:


for t in sub:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_grams = result_grams.append({'player-1':new_list[0], 'player-2':new_list[2],'player-3':new_list[1],'player-4':new_list[2], 'avg':0.0}, ignore_index=True)
        continue
    for index, row in df.iterrows():
        for ind, p in enumerate(players):
                if(df.iloc[index][p] == new_list[0] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[1] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[2] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[3] ):
                    count = count + df.iloc[index][player_scores[ind]]
    avg = count/df.shape[0]
    result_grams = result_grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'player-4':new_list[3], 'avg':avg}, ignore_index=True)


# In[19]:


result_grams.head(100)


# In[20]:


result_grams.to_csv('F:/8TH SEM/CO425-FYP/combined_results/Zimbabwe/zimbabwe_4g.csv',sep=',')        

