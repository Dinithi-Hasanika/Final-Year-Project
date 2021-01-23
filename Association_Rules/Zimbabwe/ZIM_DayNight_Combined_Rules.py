#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import numpy as np
import math


# In[4]:


match_data = pd.read_csv('F:/8TH SEM/CO425-FYP/My FYP-dos/Association Rules/Zimbabwe/ZIM_data.csv')

match_data.head()


# In[5]:


del match_data["Home"]
del match_data["Bat"]
del match_data["Toss"]
del match_data["Opposition"]


# In[6]:


match_data


# In[7]:


match_data['Day_Night'].unique() #check the unique Day_Night types


# In[8]:


player_combo = [] #list of lists match players and result
for i in range(0, 77):
    rowItem = []
    for j in range(0, 13):
        rowItem.append(str(match_data.values[i,j]))
    player_combo.append(rowItem)


# In[9]:


# player_combo


# In[10]:


te = TransactionEncoder()
te_ary = te.fit(player_combo).transform(player_combo)
match_df_freq = pd.DataFrame(te_ary, columns=te.columns_)


# In[11]:


match_df_freq


# In[12]:


match_sup = apriori(match_df_freq, min_support=0.1,use_colnames=True)
match_sup


# In[13]:


rules= association_rules(match_sup, metric="lift", min_threshold=1)


# In[14]:


rules


# In[15]:


won_rules = rules[(rules['consequents'] == {"won"})]


# In[16]:


won_rules


# In[18]:


won_rules.values[0,:]


# In[19]:


col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
DN_won_rules = pd.DataFrame(columns = col_names)


# In[20]:


i = 0
for x in won_rules['antecedents']:
    for y in x:
        if y == 'DN':
            #print(won_rules.values[i,0])
            DN_won_rules = DN_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
    i = i + 1


# In[21]:


DN_won_rules #no rules


# In[22]:


DN_won_rules.to_csv('F:/8TH SEM/CO425-FYP/My FYP-dos/Association Rules/Zimbabwe/DN_won_rules.csv')


# In[23]:


col_names = ["antecedents","consequents","antecedent support","consequent support","support","confidence","lift","leverage","conviction"]
D_won_rules = pd.DataFrame(columns = col_names)


# In[24]:


i = 0
for x in won_rules['antecedents']:
    for y in x:
        if y == 'D':
            #print(won_rules.values[i,0])
            D_won_rules = D_won_rules.append({'antecedents':won_rules.values[i,0],"consequents":won_rules.values[i,1],"antecedent support":won_rules.values[i,2],"consequent support":won_rules.values[i,3],"support":won_rules.values[i,4],"confidence":won_rules.values[i,5],"lift":won_rules.values[i,6],"leverage":won_rules.values[i,7],"conviction":won_rules.values[i,8]},ignore_index=True)
    i = i + 1


# In[25]:


D_won_rules


# In[26]:


D_won_rules.to_csv('F:/8TH SEM/CO425-FYP/My FYP-dos/Association Rules/Zimbabwe/D_won_rules.csv')

