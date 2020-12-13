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
data = pd.read_csv('bdesh.csv')


# In[3]:


data.head()


# In[4]:


players = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11']
player_scores = ['p1-s','p2-s','p3-s','p4-s','p5-s','p6-s','p7-s','p8-s','p9-s','p10-s','p11-s']


# In[5]:


x = set()


# In[6]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[7]:


print(x)


# In[8]:


len(x)


# In[9]:


unique_list = list(x)
print(unique_list)    


# In[10]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[11]:


dictionary = dict()

for indx, name in enumerate(unique_list):
    count = 0
    sum = 0
    for index, row in data.iterrows():
        for ind, p in enumerate(players):
                if(data.iloc[index][p] == name ):
#                     print(name)
                    sum = sum + data.iloc[index][player_scores[ind]] 
                    count += 1
    avg = round((sum/count),2)
    print(name," : sum=",sum," , count=",count," , average=",round(avg,2))    
    dictionary[name] = avg
    result = result.append({'player_name':name, 'sum':sum, 'avg':avg}, ignore_index=True)
    
print(dictionary)


# In[12]:


# 2 grams - find beautiful combinations


# In[26]:


#load data file
data2grams = pd.read_csv('bdesh2grams.csv')


# In[27]:


data2grams.head()


# In[28]:


data2grams.shape


# In[29]:


data2grams = data2grams[data2grams.avg != 0.0]


# In[30]:


data2grams.head()


# In[31]:


data2grams.shape


# In[32]:


data2grams = data2grams.reset_index(drop=True)


# In[33]:


data2grams.head()


# In[37]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

bdesh_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[38]:


for index, row in data2grams.iterrows():
    player1 = data2grams.iloc[index]['player-1']
    player2 = data2grams.iloc[index]['player-2']
    combined = data2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        bdesh_beautiful2grams = bdesh_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[39]:


bdesh_beautiful2grams.head()


# In[40]:


bdesh_beautiful2grams.shape


# In[41]:


bdesh_beautiful2grams.to_csv('bdesh_beautiful2grams.csv')


# In[42]:


# 3 grams - find beautiful combinations


# In[43]:


#load data file
data3grams = pd.read_csv('bdesh3grams.csv')


# In[44]:


data3grams.head()


# In[45]:


data3grams.shape


# In[46]:


data3grams = data3grams[data3grams.avg != 0.0]


# In[47]:


data3grams.shape


# In[48]:


data3grams.head()


# In[49]:


data3grams = data3grams.reset_index(drop=True)


# In[50]:


new_column_names = ["player-1", "player-2", "player-3", "combined_avg","sum_of_individual"]

bdesh_beautiful3grams = pd.DataFrame(columns = new_column_names)


# In[53]:


for index, row in data3grams.iterrows():
    player1 = data3grams.iloc[index]['player-1']
    player2 = data3grams.iloc[index]['player-2']
    player3 = data3grams.iloc[index]['player-3']
    combined = data3grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)
    if(combined > individual_avg_sum):
        bdesh_beautiful3grams = bdesh_beautiful3grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[54]:


bdesh_beautiful3grams.head()


# In[55]:


bdesh_beautiful3grams.shape


# In[56]:


bdesh_beautiful3grams.to_csv('bdesh_beautiful3grams.csv')


# In[57]:


# 4 grams - find beautiful combinations


# In[59]:


#load data file
data4grams = pd.read_csv('bdesh4grams.csv')


# In[60]:


data4grams.head()


# In[61]:


data4grams.shape


# In[62]:


data4grams = data4grams[data4grams.avg != 0.0]


# In[63]:


data4grams.shape


# In[64]:


data4grams = data4grams.reset_index(drop=True)


# In[65]:


new_column_names = ["player-1", "player-2", "player-3", "player-4", "combined_avg","sum_of_individual"]

bdesh_beautiful4grams = pd.DataFrame(columns = new_column_names)


# In[66]:


for index, row in data4grams.iterrows():
    player1 = data4grams.iloc[index]['player-1']
    player2 = data4grams.iloc[index]['player-2']
    player3 = data4grams.iloc[index]['player-3']
    player4 = data4grams.iloc[index]['player-4']
    combined = data4grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)
    if(combined > individual_avg_sum):
        bdesh_beautiful4grams = bdesh_beautiful4grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player-4':player4,'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[67]:


bdesh_beautiful4grams.head()


# In[68]:


bdesh_beautiful4grams.shape


# In[69]:


bdesh_beautiful4grams.to_csv('bdesh_beautiful4grams.csv')


# In[ ]:




