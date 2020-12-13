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
data = pd.read_csv('afg.csv')


# In[3]:


data.head()


# In[4]:


x = set()
print(x)


# In[5]:


players = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11']


# In[6]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[7]:


print(x)


# In[8]:


player_scores = ['p1-s','p2-s','p3-s','p4-s','p5-s','p6-s','p7-s','p8-s','p9-s','p10-s','p11-s']


# In[8]:


print(len(x))


# In[9]:


import itertools 
# def findsubsets(s, n): 
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 


# In[10]:


sub2 = findsubsets(x,2)


# In[12]:


## 2- grams


# In[11]:


column_names = ["player-1", "player-2", "avg"]

result_2grams = pd.DataFrame(columns = column_names)


# In[13]:


for t in sub2:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_2grams = result_2grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'avg':0.0}, ignore_index=True)
        continue
    for index, row in df.iterrows():
        for ind, p in enumerate(players):
                if(df.iloc[index][p] == new_list[0] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[1] ):
                    count = count + df.iloc[index][player_scores[ind]]
    avg = count/df.shape[0]
    result_2grams = result_2grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'avg':avg}, ignore_index=True)


# In[15]:


result_2grams.head(25)


# In[16]:


result_2grams.to_csv('afg2grams.csv')


# In[17]:


# 3-grams


# In[18]:


sub3 = findsubsets(x,3)


# In[19]:


column_names = ["player-1", "player-2","player-3", "avg"]

result_3grams = pd.DataFrame(columns = column_names)


# In[20]:


for t in sub3:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_3grams = result_3grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'avg':0.0}, ignore_index=True)
        continue
    for index, row in df.iterrows():
        for ind, p in enumerate(players):
                if(df.iloc[index][p] == new_list[0] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[1] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[2] ):
                    count = count + df.iloc[index][player_scores[ind]]
    avg = count/df.shape[0]
    result_3grams = result_3grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'avg':avg}, ignore_index=True)


# In[21]:


result_3grams.head(25)


# In[22]:


result_3grams.to_csv('afg3grams.csv')


# In[23]:


#4 grams


# In[16]:


sub4 = findsubsets(x,4)


# In[27]:


column_names = ["player-1", "player-2","player-3", "player-4", "avg"]

result_4grams = pd.DataFrame(columns = column_names)


# In[28]:


for t in sub4:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_4grams = result_4grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'player-4':new_list[3], 'avg':0.0}, ignore_index=True)
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
    result_4grams = result_4grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'player-4':new_list[3], 'avg':avg}, ignore_index=True)


# In[29]:


result_4grams.head(25)


# In[30]:


result_4grams.to_csv('afg4grams.csv')


# In[31]:


#5-grams


# In[32]:


sub5 = findsubsets(x,5)


# In[34]:


column_names = ["player-1", "player-2","player-3", "player-4", "player-5", "avg"]

result_5grams = pd.DataFrame(columns = column_names)


# In[35]:


for t in sub5:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_5grams = result_5grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'player-4':new_list[3], 'player-5':new_list[4], 'avg':0.0}, ignore_index=True)
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
                if(df.iloc[index][p] == new_list[4] ):
                    count = count + df.iloc[index][player_scores[ind]]
    avg = count/df.shape[0]
    result_5grams = result_5grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'player-4':new_list[3], 'player-5':new_list[4], 'avg':avg}, ignore_index=True)


# In[36]:


result_5grams.head(25)


# In[37]:


result_5grams.to_csv('afg5grams.csv')


# In[38]:


#6 grams 


# In[10]:


sub6 = findsubsets(x,6)


# In[11]:


column_names = ["player-1", "player-2","player-3", "player-4", "player-5", "player-6", "avg"]

result_6grams = pd.DataFrame(columns = column_names)


# In[15]:


print(len(sub6))


# In[17]:


print(len(sub4))


# In[12]:


for t in sub6:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        result_6grams = result_6grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'player-4':new_list[3], 'player-5':new_list[4], 'avg':0.0}, ignore_index=True)
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
                if(df.iloc[index][p] == new_list[4] ):
                    count = count + df.iloc[index][player_scores[ind]]
                if(df.iloc[index][p] == new_list[5] ):
                    count = count + df.iloc[index][player_scores[ind]]
    avg = count/df.shape[0]
    result_6grams = result_6grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'player-4':new_list[3], 'player-5':new_list[4], 'avg':avg}, ignore_index=True)


# In[ ]:




