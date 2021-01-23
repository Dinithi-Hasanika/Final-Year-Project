#!/usr/bin/env python
# coding: utf-8

# In[4]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[5]:


match_data = pd.read_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/SL.csv')


# In[6]:


#print the dataset
match_data.head()


# In[7]:


del match_data["Innings ID"]
del match_data["Start Date"]
del match_data["Team"]
del match_data["Day_Night"]
del match_data["Home"]
del match_data["Ground"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]


# In[8]:


#print the dataset
match_data


# In[11]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 6):
    rowItem = []
    for j in range(0, 12):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[12]:


print(player_combo)


# In[13]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[14]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
print(match_sup)


# In[15]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[16]:


#print the association rules
rules


# In[17]:


#remove the one itemsets
#obtain the final winning combinations
rules = rules[(rules['antecedents'].str.len() > 1)] #Here won_rules['antecedents'] is a frozenset


# In[18]:


rules


# In[19]:


#extract only the combinations occured at a winning match
won_rules = rules[(rules['consequents'] == {"won"})]


# In[20]:


won_rules


# In[21]:


#sorting by confidence --- descending order
won_rules.sort_values(by ='confidence', ascending = False, inplace = True)


# In[22]:


won_rules


# In[23]:


#For example let's take the first rule
#if B Kumar, YS Chahal, KM Jadhav, MS Dhoni then won
#112 no of matches have played by the indian team from 2015 to 2020
#here the support is 0.205357 = x/112
#therefore no. of times the antecedent occurs = 0.205357*112 = approx 23 = x
#confidence = 0.958333 = y/23
#No of times the correct rule occured from the 23 instances is = 0.958333*23 = aprox 22 = y


# In[24]:


#sorting by support --- descending order
#won_rules.sort_values(by ='support', ascending = False, inplace = True)


# In[25]:


#won_rules


# In[26]:


#Support is an indication of how frequently the itemset appears in the dataset.
#Confidence is an indication of how often the rule has been found to be true.


# In[27]:


support=won_rules['support']
confidence=won_rules['confidence']


# In[28]:


import random
import matplotlib.pyplot as plt
 
plt.scatter(support, confidence,marker="*")
plt.xlabel('support')
plt.ylabel('confidence') 
plt.show()


# In[29]:


#select all the rules where antecedent contains 'RG Sharma'
#won_rules[(won_rules['antecedents'].apply(lambda x: 'RG Sharma' in str(x)))]


# In[30]:


won_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won_rules.csv')


# In[31]:


won_2_rules = won_rules[(won_rules['antecedents'].str.len() == 2)]


# In[32]:


won_2_rules


# In[33]:


won_2_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won2_rules.csv')


# In[34]:


won_3_rules = won_rules[(won_rules['antecedents'].str.len() == 3)]


# In[35]:


won_3_rules


# In[36]:


won_3_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won3_rules.csv')


# In[37]:


won_4_rules = won_rules[(won_rules['antecedents'].str.len() == 4)]


# In[38]:


won_4_rules


# In[39]:


won_4_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won4_rules.csv')


# In[40]:


won_5_rules = won_rules[(won_rules['antecedents'].str.len() == 5)]
won_5_rules


# In[41]:


won_5_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won5_rules.csv')


# In[42]:


won_6_rules = won_rules[(won_rules['antecedents'].str.len() == 6)]
won_6_rules


# In[43]:


won_6_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won6_rules.csv')


# In[44]:


won_7_rules = won_rules[(won_rules['antecedents'].str.len() == 7)]
won_7_rules


# In[45]:


won_7_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won7_rules.csv')


# In[46]:


won_8_rules = won_rules[(won_rules['antecedents'].str.len() == 8)]
won_8_rules


# In[47]:


won_8_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won8_rules.csv')


# In[48]:


won_9_rules = won_rules[(won_rules['antecedents'].str.len() == 9)]
won_9_rules


# In[49]:


won_10_rules = won_rules[(won_rules['antecedents'].str.len() == 10)]
won_10_rules


# In[50]:


won_10_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won10_rules.csv')


# In[51]:


won_11_rules = won_rules[(won_rules['antecedents'].str.len() == 11)]
won_11_rules


# In[52]:


won_11_rules.to_csv('E:/University Works/4th Year/Semester 8/CO425 - Final Year Project 2/Association_Rules/1996_World_Cup/SL/1996_SL_won11_rules.csv')


# In[ ]:




