#!/usr/bin/env python
# coding: utf-8

# In[98]:


import pandas as pd
import numpy as np
import math


# In[99]:


won_data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/India/won2mod.csv')


# In[100]:


won_data


# In[101]:


#making an array of arrays containing p1,p2, support,confidence
#a python list can hold different data types
#player names have different orders therefore it is taken as a set so that it will be easy when comparing
#since sets do not care about the order of element when checking the equility
wonRules = []
for i in range(0, 75):
    rowItem = []
    rowset = set()
    for j in range(0, 2):
        rowset.add(won_data.values[i,j])
    rowItem.append(rowset)
    rowItem.append(won_data.values[i,5])
    rowItem.append(won_data.values[i,6])
    wonRules.append(rowItem)


# In[102]:


wonRules


# In[103]:


india_beautiful2grams = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Batsman/India/india_beautiful2grams.csv')


# In[104]:


india_beautiful2grams


# In[105]:


del india_beautiful2grams["Unnamed: 0"]


# In[106]:


india_beautiful2grams


# In[107]:


#making an array of arrays containing player-1,player-2, combined_avg,sum_of_individual
#player names have different orders therefore it is taken as a set so that it will be easy when comparing
#since sets do not care about the order of element when checking the equility
bat = []
for i in range(0, 275):
    rowItem = []
    rowset = set()
    for j in range(0, 2):
        rowset.add(india_beautiful2grams.values[i,j])
    rowItem.append(rowset)
    rowItem.append(india_beautiful2grams.values[i,2])
    rowItem.append(india_beautiful2grams.values[i,3])
    bat.append(rowItem)


# In[108]:


bat


# In[109]:


#comparing equal combinations in datasets of wonRules and bat
fin = []
for i in range(0,75):
    rowItem = []
    for j in range(0,275):
        x = 0
        if wonRules[i][0] == bat[j][0]:
            rowItem.append(wonRules[i][0])
            rowItem.append(wonRules[i][1])
            rowItem.append(wonRules[i][2])
            rowItem.append(bat[j][1])
            rowItem.append(bat[j][2])
            x = 1
        if x == 1:
            fin.append(rowItem)


# In[110]:


fin


# In[111]:


len(fin)


# In[112]:


new_column_names = ["player-1", "player-2","support","confidence","combined_avg","sum_of_individual"]


# In[113]:


won2RulesCompare = pd.DataFrame(columns = new_column_names)


# In[114]:


for i in range(0,31):
    players = []
    for p in fin[i][0]:
        players.append(p)
    won2RulesCompare = won2RulesCompare.append({"player-1":players[0],
                                                    "player-2":players[1],
                                                    "support":fin[i][1],
                                                    "confidence":fin[i][2],
                                                    "combined_avg":fin[i][3],
                                                    "sum_of_individual":fin[i][4]},ignore_index=True)


# In[115]:


won2RulesCompare


# In[116]:


won2RulesCompare.to_excel('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/CompareRulesBatAvg/India/won2RulesCompare.xlsx')


# In[ ]:




