#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# # Finding individual averages of batsmen

# In[2]:


#load data file
data = pd.read_csv('Zimbabwe.csv')


# In[3]:


data.head()


# In[4]:


players = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11']
player_scores = ['p1-s','p2-s','p3-s','p4-s','p5-s','p6-s','p7-s','p8-s','p9-s','p10-s','p11-s']


# In[5]:


x = set()


# In[6]:


# finding unique players
for i in players:
    for j in range(len(data[i].unique())):
        x.add(data[i].unique()[j])


# In[7]:


print(x)


# In[8]:


len(x)


# In[9]:


#set -> list
unique_list = list(x)
print(unique_list)    


# In[10]:


column_names = ["player_name", "sum", "avg"]

result = pd.DataFrame(columns = column_names)


# In[11]:


# finding the individual averages of players=> total score/no.of matches played
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


result.head(13)


# # 6 grams - Total runs scored

# In[14]:


data.head()


# In[15]:


import itertools 
# def findsubsets(s, n): 
def findsubsets(s, n): 
    return [set(i) for i in itertools.combinations(s, n)] 


# In[16]:


len(findsubsets(x,6))


# In[17]:


sub = findsubsets(x,6)


# In[18]:


# column_names = ["player-1", "player-2","player-3", "player-4","player-5", "player-6", "player-7","player-8", "player-9","player-10", "player-11"]
column_names = ["player-1", "player-2","player-3", "player-4","player-5", "player-6"]
result_grams = pd.DataFrame(columns = column_names)


# In[19]:


for t in sub:
    new_list = list(t)
    df = data[np.equal.outer(data.to_numpy(copy=False),  new_list).any(axis=1).all(axis=1)]
    df = df.reset_index(drop=True)
    result_grams = result_grams.append({'player-1':new_list[0], 'player-2':new_list[1], 'player-3':new_list[2], 'player-4':new_list[3], 'player-5':new_list[4], 'player-6':new_list[5]}, ignore_index=True)


# In[20]:


result_grams


# In[21]:


new_column_names = ["player-1", "player-2","player-3", "player-4","player-5", "player-6","sum_of_individual"]

zimb_sumofInd_6grams = pd.DataFrame(columns = new_column_names)


# In[22]:


for index, row in result_grams.iterrows():
    player1 = result_grams.iloc[index]['player-1']
    player2 = result_grams.iloc[index]['player-2']
    player3 = result_grams.iloc[index]['player-3']
    player4 = result_grams.iloc[index]['player-4']
    player5 = result_grams.iloc[index]['player-5']
    player6 = result_grams.iloc[index]['player-6']
    individual_avg_sum = dictionary.get(player1)+dictionary.get(player2)+dictionary.get(player3)+dictionary.get(player4)+dictionary.get(player5)+dictionary.get(player6)
    zimb_sumofInd_6grams = zimb_sumofInd_6grams.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player4-':player4, 'player5-':player5, 'player-6':player6,'sum_of_individual':individual_avg_sum}, ignore_index=True)


# In[23]:


zimb_sumofInd_6grams.head()


# In[24]:


zimb_sumofInd_6grams.shape


# # Bowlers - runs conceded- individual

# In[25]:


#load data file
data_bw = pd.read_csv('ZIMB_BW.csv')


# In[26]:


data_bw.head()


# In[27]:


data_bw = data_bw.loc[:, ~data_bw.columns.str.contains('^Unnamed')]
data_bw


# In[28]:


bowlers = ['p1','p2','p3','p4','p5','p6','p7','p8']
bowler_scores = ['s1','s2','s3','s4','s5','s6','s7','s8']


# In[29]:


x_bw = set()

for i in bowlers:
    for j in range(len(data_bw[i].unique())):
        x_bw.add(data_bw[i].unique()[j])
        
print(x_bw)


# In[30]:


len(x_bw)


# In[31]:


x_bw.remove('-')
len(x_bw)


# In[32]:


unique_list_bw = list(x_bw)
print(unique_list_bw) 


# In[33]:


column_names_bw = ["bowler_name", "sum_runs_conc_indiv", "avg"]

result_bw = pd.DataFrame(columns = column_names_bw)


# In[34]:


dictionary_bw_avg = dict()
dictionary_bw_sum = dict()
for indx, name in enumerate(unique_list_bw):
    count = 0
    sum = 0
    for index, row in data_bw.iterrows():
        for ind, p in enumerate(bowlers):
                if(data_bw.iloc[index][p] == name ):
                    sum = sum + data_bw.iloc[index][bowler_scores[ind]] 
                    count += 1
    avg = round((sum/count),2)
    print(name," : sum=",sum," , count=",count," , average=",round(avg,2)) 
    dictionary_bw_sum[name] = sum
    dictionary_bw_avg[name] = avg
    result_bw = result_bw.append({'bowler_name':name, 'sum_runs_conc_indiv':sum, 'avg':avg}, ignore_index=True)
    
print(dictionary_bw_sum)


# # team runs scores VS bowlers runs given

# In[35]:


zimb_sumofInd_6grams #team scores(avg)


# In[36]:


column_names_all = ["player-1", "player-2","player-3", "player-4","player-5", "player-6","sum_of_individual", "totalRunsConceded_bw"]
analyse_all = pd.DataFrame(columns = column_names_all)

column_names_beutiful = ["player-1", "player-2","player-3", "player-4","player-5", "player-6","sum_of_individual", "totalRunsConceded_bw"]
analyse_beautiful = pd.DataFrame(columns = column_names_beutiful)


# In[37]:


for index, row in zimb_sumofInd_2grams.iterrows():
    player1 = zimb_sumofInd_6grams.iloc[index]['player-1']
    player2 = zimb_sumofInd_6grams.iloc[index]['player-2']
    player3 = zimb_sumofInd_6grams.iloc[index]['player-3']
    player4 = zimb_sumofInd_6grams.iloc[index]['player-4']
    player5 = zimb_sumofInd_6grams.iloc[index]['player-5']
    player6 = zimb_sumofInd_6grams.iloc[index]['player-6']
    sum_of_indiv = zimb_sumofInd_6grams.iloc[index]['sum_of_individual']
    player1_bw_runs_conc = dictionary_bw_avg.get(player1) 
    player2_bw_runs_conc = dictionary_bw_avg.get(player2)
#     print('player1 :',player1_bw_runs_conc)
#     print('player2 :',player2_bw_runs_conc)
    
    if player1_bw_runs_conc is None:
        player1_bw_runs_conc = 0
    
    if player2_bw_runs_conc is None:
        player2_bw_runs_conc = 0 
        
    totalRunsConceded_bw = player1_bw_runs_conc+player2_bw_runs_conc
    analyse_all = analyse_all.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player4-':player4, 'player5-':player5, 'player-6':player6,'sum_of_individual':sum_of_indiv, 'totalRunsConceded_bw':totalRunsConceded_bw}, ignore_index=True)
    
    if(sum_of_indiv > totalRunsConceded_bw):
        analyse_beautiful = analyse_beautiful.append({'player-1':player1, 'player-2':player2,'player-3':player3, 'player4-':player4, 'player5-':player5, 'player-6':player6,'sum_of_individual':sum_of_indiv, 'totalRunsConceded_bw':totalRunsConceded_bw}, ignore_index=True)


# In[38]:


analyse_all.head(400)


# In[39]:


analyse_all.shape


# In[40]:


analyse_beautiful.head()


# In[41]:


analyse_beautiful.shape


# In[42]:


analyse_all.to_csv('analyse_all_6g.csv',sep=',')  


# In[43]:


analyse_beautiful.to_csv('analyse_beautiful_6g.csv',sep=',')  

