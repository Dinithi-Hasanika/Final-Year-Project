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


# In[13]:


#load data file
data2grams = pd.read_csv('afg2grams.csv')


# In[14]:


data2grams.head()


# In[15]:


data2grams.shape


# In[16]:


data2grams = data2grams[data2grams.avg != 0.0]


# In[17]:


data2grams.head()


# In[18]:


data2grams.shape


# In[19]:


data2grams = data2grams.reset_index(drop=True)


# In[20]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

afg_beautiful2grams = pd.DataFrame(columns = new_column_names)


# In[21]:


for index, row in data2grams.iterrows():
    player1 = data2grams.iloc[index]['player-1']
    player2 = data2grams.iloc[index]['player-2']
    combined = data2grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    if(combined > individual_avg_sum):
        afg_beautiful2grams = afg_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[22]:


afg_beautiful2grams.head()


# In[23]:


afg_beautiful2grams.shape


# In[24]:


afg_beautiful2grams.to_csv('afg_beautiful2grams.csv')


# In[25]:


# 3 grams - find beautiful combinations


# In[26]:


#load data file
data3grams = pd.read_csv('afg3grams.csv')


# In[27]:


data3grams.head()


# In[28]:


data3grams.shape


# In[29]:


data3grams = data3grams[data3grams.avg != 0.0]


# In[30]:


data3grams.shape


# In[31]:


data3grams = data3grams.reset_index(drop=True)


# In[32]:


new_column_names = ["player-1", "player-2", "player-3", "combined_avg","sum_of_individual"]

afg_beautiful3grams = pd.DataFrame(columns = new_column_names)


# In[33]:


for index, row in data3grams.iterrows():
    player1 = data3grams.iloc[index]['player-1']
    player2 = data3grams.iloc[index]['player-2']
    player3 = data3grams.iloc[index]['player-3']
    combined = data3grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)
    if(combined > individual_avg_sum):
        afg_beautiful3grams = afg_beautiful3grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[34]:


afg_beautiful3grams.head()


# In[35]:


afg_beautiful3grams.shape


# In[36]:


afg_beautiful3grams.to_csv('afg_beautiful3grams.csv')


# In[37]:


# 4 grams - find beautiful combinations


# In[38]:


#load data file
data4grams = pd.read_csv('afg4grams.csv')


# In[39]:


data4grams.head()


# In[40]:


data4grams.shape


# In[41]:


data4grams = data4grams[data4grams.avg != 0.0]


# In[42]:


data4grams.shape


# In[43]:


data4grams = data4grams.reset_index(drop=True)


# In[44]:


new_column_names = ["player-1", "player-2", "player-3", "player-4", "combined_avg","sum_of_individual"]

afg_beautiful4grams = pd.DataFrame(columns = new_column_names)


# In[45]:


for index, row in data4grams.iterrows():
    player1 = data4grams.iloc[index]['player-1']
    player2 = data4grams.iloc[index]['player-2']
    player3 = data4grams.iloc[index]['player-3']
    player4 = data4grams.iloc[index]['player-4']
    combined = data4grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)
    if(combined > individual_avg_sum):
        afg_beautiful4grams = afg_beautiful4grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player-4':player4,'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[46]:


afg_beautiful4grams.head()


# In[47]:


afg_beautiful4grams.shape


# In[48]:


afg_beautiful4grams.to_csv('afg_beautiful4grams.csv')


# In[49]:


# 5 grams - find beautiful combinations


# In[51]:


#load data file
data5grams = pd.read_csv('afg5grams.csv')


# In[52]:


data5grams.head()


# In[53]:


data5grams.shape


# In[54]:


data5grams = data5grams[data5grams.avg != 0.0]


# In[55]:


data5grams.shape


# In[57]:


data5grams = data5grams.reset_index(drop=True)


# In[59]:


new_column_names = ["player-1", "player-2", "player-3", "player-4", "player-5", "combined_avg","sum_of_individual"]

afg_beautiful5grams = pd.DataFrame(columns = new_column_names)


# In[61]:


for index, row in data5grams.iterrows():
    player1 = data5grams.iloc[index]['player-1']
    player2 = data5grams.iloc[index]['player-2']
    player3 = data5grams.iloc[index]['player-3']
    player4 = data5grams.iloc[index]['player-4']
    player5 = data5grams.iloc[index]['player-5']
    combined = data5grams.iloc[index]['avg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)+dictionary.get(player5)
    if(combined > individual_avg_sum):
        afg_beautiful5grams = afg_beautiful5grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player-4':player4, 'player-5':player5,'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[62]:


afg_beautiful5grams.shape


# In[63]:


afg_beautiful5grams.head()


# In[64]:


afg_beautiful5grams.to_csv('afg_beautiful5grams.csv')


# In[ ]:




