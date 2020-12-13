#!/usr/bin/env python
# coding: utf-8

# In[1]:


from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1peLpNFoEu8NHtVPttJXz4-aScixYu5dh_-6gYPOi9rQ/edit#gid=670066504')


# In[4]:


sheet = wb.worksheet('bt_data')


# In[5]:


data = sheet.get_all_values()


# In[6]:


df = pd.DataFrame(data)
df.columns = df.iloc[0]
df = df.iloc[1:]


# In[7]:


df.head()


# In[8]:


import sklearn
print(sklearn.__version__)


# In[9]:


from sklearn.linear_model import LinearRegression
from matplotlib import pyplot


# In[10]:


print(df.info())


# In[11]:


df["Mat"]= df["Mat"].astype(float)
df["Inns"]= df["Inns"].astype(float)
df["NO"]= df["NO"].astype(float)
df["HS_NO"]= df["HS_NO"].astype(float)
df["Ave"]= df["Ave"].astype(float)
df["BF"]= df["BF"].astype(float)
df["SR"]= df["SR"].astype(float)
df["100"]= df["100"].astype(float)
df["50"]= df["50"].astype(float)
df["0"]= df["0"].astype(float)
df["Last 4 match runs mean"]= df["Last 4 match runs mean"].astype(float)
df["Man of the match"]= df["Man of the match"].astype(float)
df["Runs"]= df["Runs"].astype(float)
df["HS"]= df["HS"].astype(float)
df["Height (cm)"]= df["Height (cm)"].astype(float)
df["Batsmen Score"]= df["Batsmen Score"].astype(float)


# In[12]:


print(df.info())


# In[13]:


from sklearn.preprocessing import LabelEncoder

label = LabelEncoder()
df['Batting Style'] = label.fit_transform(df['Batting Style'])


# In[14]:


df.head()


# In[15]:


from sklearn.ensemble import RandomForestClassifier


# In[16]:


carrear_feature_names = ["Man of the match", "Last 4 match runs mean", "Height (cm)", "Batting Style", "Ave", "NO", "HS", "HS_NO", "SR", "100", "50", "0"]
X_carrear = df[carrear_feature_names]
Y = df["Runs"]


# In[17]:


#split the data set as training set and test set randomly
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_carrear, Y, random_state=0)


# In[18]:


#apply scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Linear Regression Carrear Features

# In[19]:


modelc_lreg = LinearRegression()


# In[20]:


modelc_lreg.fit(X_train, y_train)


# In[21]:


importance_lreg = modelc_lreg.coef_


# In[22]:


for i,v in enumerate(importance_lreg):
	print('Feature:%0d -> %s, Score: %.5f' % (i,carrear_feature_names[i],v))


# In[23]:


pyplot.bar([x for x in range(len(importance_lreg))], importance_lreg)
pyplot.xticks(np.arange(len(carrear_feature_names)), carrear_feature_names,rotation='vertical')
pyplot.show()


# In[24]:


print('Accuracy of Linear regression classifier on training set: {:.2f}'
     .format(modelc_lreg.score(X_train, y_train)))
print('Accuracy of Linear regression classifier on test set: {:.2f}'
     .format(modelc_lreg.score(X_test, y_test)))


# Random Forest Carrear features 

# In[25]:


modelrfc = RandomForestClassifier()
modelrfc.fit(X_train, y_train)


# In[26]:


importancerfc = modelrfc.feature_importances_


# In[27]:


for i,v in enumerate(importancerfc):
	print('Feature:%0d -> %s, Score: %.5f' % (i,carrear_feature_names[i],v))


# In[28]:


pyplot.bar([x for x in range(len(importancerfc))], importancerfc)
pyplot.xticks(np.arange(len(carrear_feature_names)), carrear_feature_names,rotation='vertical')
pyplot.show()


# In[29]:


print('Accuracy of Linear regression classifier on training set: {:.2f}'
     .format(modelrfc.score(X_train, y_train)))
print('Accuracy of Linear regression classifier on test set: {:.2f}'
     .format(modelrfc.score(X_test, y_test)))


# Xgboost Carrear Features

# In[30]:


from xgboost import XGBRegressor
# define the model
modelxg = XGBRegressor()
# fit the model
modelxg.fit(X_train, y_train)
# get importance
importancexg = modelxg.feature_importances_
# summarize feature importance
for i,v in enumerate(importancexg):
	print('Feature: %0d, -> %s Score: %.5f' % (i,carrear_feature_names[i] ,v))
# plot feature importance
plt.bar([x for x in range(len(importancexg))], importancexg)
pyplot.xticks(np.arange(len(carrear_feature_names)), carrear_feature_names,rotation='vertical')
plt.show()


# In[31]:


print('Accuracy of xgboost classifier on training set: {:.2f}'
     .format(modelxg.score(X_train, y_train)))
print('Accuracy of xgboost classifier on test set: {:.2f}'
     .format(modelxg.score(X_test, y_test)))


# Permutation Carrear Features

# In[32]:


from sklearn.neighbors import KNeighborsRegressor
from sklearn.inspection import permutation_importance

# define the model
knn = KNeighborsRegressor()
# fit the model
knn.fit(X_train, y_train)
# perform permutation importance
results = permutation_importance(knn, X_train, y_train, scoring='neg_mean_squared_error')
# get importance
importance_k = results.importances_mean
# summarize feature importance
for i,v in enumerate(importance_k):
	print('Feature: %0d, -> %s Score: %.5f' % (i,carrear_feature_names[i],v))
# plot feature importance
plt.bar([x for x in range(len(importance_k))], importance_k)
pyplot.xticks(np.arange(len(carrear_feature_names)), carrear_feature_names,rotation='vertical')
plt.show()


# In[33]:


print('Accuracy of knn classifier on training set: {:.2f}'
     .format(knn.score(X_train, y_train)))
print('Accuracy of knn classifier on test set: {:.2f}'
     .format(knn.score(X_test, y_test)))


# CART carrear features

# In[34]:


from sklearn.tree import DecisionTreeRegressor
# from matplotlib import pyplot

# define the model
modelcart = DecisionTreeRegressor()
# fit the model
modelcart.fit(X_train, y_train)
# get importance
importancecart = modelcart.feature_importances_
# summarize feature importance
for i,v in enumerate(importancecart):
	print('Feature: %0d,-> %s Score: %.5f' % (i,carrear_feature_names[i],v))
# plot feature importance
pyplot.bar([x for x in range(len(importancecart))], importancecart)
pyplot.xticks(np.arange(len(carrear_feature_names)), carrear_feature_names,rotation='vertical')
pyplot.show()


# In[35]:


print('Accuracy of cart classifier on training set: {:.2f}'
     .format(modelcart.score(X_train, y_train)))
print('Accuracy of cart classifier on test set: {:.2f}'
     .format(modelcart.score(X_test, y_test)))


# In[36]:


Test_names = ['Linear regression', 'Randomforest', 'CART', 'Xgboost',
              'k-neighbors']
name_code = ['LR', 'RF', 'CART', 'xG', 'k-N']

training = []
test = []

training.append(modelc_lreg.score(X_train, y_train))
training.append(modelrfc.score(X_train, y_train)) 
training.append(modelcart.score(X_train, y_train))
training.append(modelxg.score(X_train, y_train))
training.append(knn.score(X_train, y_train))

test.append(modelc_lreg.score(X_test, y_test))
test.append(modelrfc.score(X_test, y_test)) 
test.append(modelcart.score(X_test, y_test))
test.append(modelxg.score(X_train, y_train))
test.append(knn.score(X_test, y_test))

plt.scatter(name_code,training,label='training')
plt.scatter(name_code,test,label='test')
plt.xlabel('Name of the test')
plt.ylabel('Accuracy for each test')
plt.legend()
plt.show()


# In[37]:


A = np.ones([len(carrear_feature_names),len(carrear_feature_names)])
for j,p in enumerate(importance_k):
  for i,v in enumerate(importance_k):
    A[j,i] = float("{:.3f}".format(p/v))
    print('Importance of %s over %s is  Score: %.3f' % (carrear_feature_names[j],carrear_feature_names[i],p/v))


# In[38]:


ar = np.array(A)
print(ar)


# In[39]:


priority = []
for row in A:
 v = 1
 for i in row:
   v = v * i
 v = v ** (1/len(carrear_feature_names))
 priority.append(v)


# In[40]:


for i in range(len(carrear_feature_names)):
  print(carrear_feature_names[i],priority[i])


# In[41]:


pr = np.array(priority)
p = sum(pr)
print(p)


# In[42]:


weights = []
for i in priority:
  value = float("{:.4f}".format(i/p))
  weights.append(value)
   


# In[43]:


for i in range(len(carrear_feature_names)):
  print(carrear_feature_names[i],weights[i])


# In[44]:


thisdict = {}
for i in range(len(carrear_feature_names)):
  thisdict[carrear_feature_names[i]] = weights[i]
print(thisdict)


# In[45]:


df['Batsmen_score'] = df['Man of the match']*thisdict['Man of the match']+df['Last 4 match runs mean']*thisdict['Last 4 match runs mean']+df['Height (cm)']*thisdict['Height (cm)']+df['Batting Style']*thisdict['Batting Style']+df['Ave']*thisdict['Ave']+df['NO']*thisdict['NO']+df['HS']*thisdict['HS']+df['HS_NO']*thisdict['HS_NO']+df['SR']*thisdict['SR']+df['100']*thisdict['100']+df['50']*thisdict['50']+df['0']*thisdict['0']


# In[46]:


df['Batsmen_score2'] = df['Man of the match']*thisdict['Man of the match']+df['Last 4 match runs mean']*thisdict['Last 4 match runs mean']+df['Height (cm)']*thisdict['Height (cm)']+df['Batting Style']*thisdict['Batting Style']+df['Ave']*thisdict['Ave']+df['NO']*thisdict['NO']+df['HS']*thisdict['HS']+df['HS_NO']*thisdict['HS_NO']+df['SR']*thisdict['SR']+df['100']*thisdict['100']+df['50']*thisdict['50']-df['0']*thisdict['0']


# In[47]:


df.head(15)


# In[48]:


df.tail(15)


# In[49]:


del df["u"]
del df["v"]
del df["w"]


# In[50]:


df.head()


# In[51]:


final_df = df.copy()


# In[52]:


final_df = final_df.sort_values(by=['Batsmen_score2'], ascending=False)


# In[54]:


final_df.head(20)


# In[55]:


df1 = final_df[['player', 'Batsmen_score2']]


# In[56]:


df1.head(20)


# In[57]:


from google.colab import files
df.to_csv('carrear_batsman_score_original.csv' , index=False)
files.download('carrear_batsman_score_original.csv')

