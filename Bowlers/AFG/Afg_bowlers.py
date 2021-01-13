#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


#load data file
data = pd.read_csv('AFG_BW.csv')


# In[30]:


data.head()


# In[31]:


data = data.loc[:, ~data.columns.str.contains('^Unnamed')]


# In[32]:


data


# In[33]:


data = data.drop(73)


# In[34]:


data


# In[6]:


players = ['p1','p2','p3','p4','p5','p6','p7']
player_scores = ['s1','s2','s3','s4','s5','s6','s7']
player_wickets = ['w1','w2','w3','w4','w5','w6','w7']


# In[35]:


x = set()


# In[36]:


for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[37]:


print(x)


# In[38]:


x.remove('-')


# In[39]:


len(x)


# In[40]:


import itertools 
# def findsubsets(s, n): 
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 


# In[41]:


#2-grams
sub2 = findsubsets(x,2)


# In[56]:


column_names = ["player-1", "player-2", "avg", "wkavg"]

result_2grams = pd.DataFrame(columns = column_names)


# In[57]:


for t in sub2:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    count = 0;
    wkcount = 0;
    df = df.reset_index(drop=True)
    isempty = df.empty
    if(isempty):
        continue
    for index, row in df.iterrows():
        for ind, p in enumerate(players):
                if(df.iloc[index][p] == new_list[0] ):
                    count = count + df.iloc[index][player_scores[ind]]
                    wkcount = wkcount + df.iloc[index][player_wickets[ind]]
                if(df.iloc[index][p] == new_list[1] ):
                    count = count + df.iloc[index][player_scores[ind]]
                    wkcount = wkcount + df.iloc[index][player_wickets[ind]]
    avg = count/df.shape[0]
    wkavg = wkcount/df.shape[0]
    result_2grams = result_2grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'avg':avg, 'wkavg':wkavg}, ignore_index=True)


# In[58]:


result_2grams.head(25)


# In[45]:


len(sub2)


# In[46]:


len(result_2grams)


# In[47]:


unique_list = list(x)
print(unique_list)  


# In[48]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[59]:


dictionary = dict()
dictionarywk = dict()
for indx, name in enumerate(unique_list):
    count = 0
    sum = 0
    wksum = 0
    for index, row in data.iterrows():
        for ind, p in enumerate(players):
                if(data.iloc[index][p] == name ):
#                     print(name)
                    sum = sum + data.iloc[index][player_scores[ind]] 
                    wksum = wksum + data.iloc[index][player_wickets[ind]] 
                    count += 1
    avg = round((sum/count),2)
    wkavg = round((wksum/count),2)
    print(name," : sum=",sum," , count=",count," , average=",round(avg,2))    
    dictionary[name] = avg
    dictionarywk[name] = wkavg
    result = result.append({'player_name':name, 'sum':sum, 'avg':avg}, ignore_index=True)
    
print(dictionary)
print(dictionarywk)


# In[77]:


new_column_names = ["player-1", "player-2", "combined_avg","sum_of_individual"]

afg_beautiful2grams = pd.DataFrame(columns = new_column_names)

new_column_names2 = ["player-1", "player-2"]

afgwk_beautiful2grams = pd.DataFrame(columns = new_column_names)
afg_beautiful2grams_both = pd.DataFrame(columns = new_column_names2)


# In[78]:


for index, row in result_2grams.iterrows():
    player1 = result_2grams.iloc[index]['player-1']
    player2 = result_2grams.iloc[index]['player-2']
    combined = result_2grams.iloc[index]['avg']
    combinedwk = result_2grams.iloc[index]['wkavg']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)
    individual_avg_wk = dictionarywk.get(player1)+dictionarywk.get(player2)
    if(combined < individual_avg_sum):
        afg_beautiful2grams = afg_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combined, 'sum_of_individual':individual_avg_sum}, ignore_index=True)
    if(combinedwk > individual_avg_wk):
        afgwk_beautiful2grams = afgwk_beautiful2grams.append({'player-1':player1, 'player-2':player2, 'combined_avg': combinedwk, 'sum_of_individual':individual_avg_wk}, ignore_index=True)
    if(combinedwk > individual_avg_wk and combined < individual_avg_sum ):
        afg_beautiful2grams_both = afg_beautiful2grams_both.append({'player-1':player1, 'player-2':player2}, ignore_index=True)
        


# In[79]:


afg_beautiful2grams.head()


# In[80]:


len(afg_beautiful2grams)


# In[81]:


#Wickets


# In[82]:


afgwk_beautiful2grams.head()


# In[83]:


len(afgwk_beautiful2grams)


# In[84]:


afg_beautiful2grams_both.head()


# In[85]:


len(afg_beautiful2grams_both)


# In[86]:


afg_beautiful2grams_both


# In[ ]:




