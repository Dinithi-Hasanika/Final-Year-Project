#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[3]:


match_data = pd.read_csv('F:/8TH SEM/CO425-FYP/My FYP-dos/Association Rules/Zimbabwe/ZIM_Position_data.csv')

match_data.head()


# In[4]:


del match_data["p1"]
del match_data["p2"]
del match_data["p3"]
del match_data["p4"]
del match_data["p5"]
del match_data["p6"]
del match_data["p7"]
del match_data["p8"]
del match_data["p9"]
del match_data["p10"]
del match_data["p11"]


# In[5]:


match_data


# In[6]:


# convert our pandas dataframe into a list of lists,
player_combo = [] #list of lists match players and result
for i in range(0, 77):
    rowItem = []
    for j in range(0, 12):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[7]:


print(player_combo)


# In[8]:


#Creating the dataframe of frequent itemsets
te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[9]:


#Define the minimum support and obtain the itemsets greater than the min support
#support = No. of times the required itemset occured / total no. of matches
match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
print(match_sup)


# In[10]:


#generate association rules
rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[11]:


#print the association rules
rules


# In[12]:


#extract only the combinations occured at a winning match
won_rules = rules[(rules['consequents'] == {"won"})]


# In[13]:


won_rules


# In[14]:


#remove the one itemsets
#obtain the final winning combinations
position_won_rules = won_rules[(won_rules['antecedents'].str.len() > 1)] #Here won_rules['antecedents'] is a frozenset


# In[15]:


#print the winning combinations
position_won_rules


# In[16]:


#finding winning combinatios with positions
#removing same player combinations because of different postions
#example: remvove antecedents with [V Kohli3,V Kohli5]
#col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
#position_won_rules = pd.DataFrame(columns = col_names)

#i = 0
#for x in won_rules['antecedents']:
#    itemDup = [] # can have duplicates
#    itemSet = set() #without duplicates
#    for y in x:
#        y[:-1]#remove the last letter from the string
#        itemDup.append(y)
#        itemSet.add(y)
        
#    if len(itemDup) == len(itemSet):
#        position_won_rules = position_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
#    i = i + 1


# In[17]:


#sorting by confidence --- descending order
position_won_rules.sort_values(by ='confidence', ascending = False, inplace = True)


# In[18]:


position_won_rules


# In[19]:


#For example let's take the first rule
#if JJ Bumrah10, V Kohli3 then won
#112 no of matches have played by the indian team from 2015 to 2020
#here the support is 0.169643 = x/112
#therefore no. of times the antecedent occurs = 0.169643*112 = approx 19 = x
#confidence = 0.904762 = y/19
#No of times the correct rule occured from the 19 instances is = 0.904762*19 = aprox 17


# In[20]:


#sorting by support --- descending order
position_won_rules.sort_values(by ='support', ascending = False, inplace = True)


# In[21]:


position_won_rules


# In[22]:


import random
import matplotlib.pyplot as plt

support=position_won_rules['support']
confidence=position_won_rules['confidence']
 
plt.scatter(support, confidence,marker="*")
plt.xlabel('support')
plt.ylabel('confidence') 
plt.show()


# In[23]:


# position_won_rules.to_csv('F:/8TH SEM/CO425-FYP/My FYP-dos/Association Rules/Zimbabwe/ZIM_position_won_rules.csv')


# In[25]:


len(player_combo)


# In[ ]:




