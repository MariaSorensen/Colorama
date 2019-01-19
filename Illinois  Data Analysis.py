#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


# Read the data
crime = pd.read_csv("Crimes_2012_to_2015.csv")


# In[3]:


# See first few rows of the data
crime.head()


# In[4]:


# keep necessary columns
crime = crime[['Arrest','Primary Type','Community Area']]


# In[5]:


# See crime value types
crime.Arrest.unique()


# In[6]:


# Recode Value


# In[7]:


crime['Arrest'] = crime['Arrest'].map({True:'Success',False:'Failure'})


# 1.how many arrests were successful and unsuccessful. 

# In[8]:


# Count arrest types
arrestcount = pd.DataFrame(crime.Arrest.value_counts())


# #### fig = plt.figure(figsize = (10,4))
# arrestcount.plot(kind='bar',title = 'Illinois Crime Arrest', ax = plt.gca())

# In[10]:


arrestcount


# 49894 arrests were successfull and 149968 arrests were unsuccessfull.

# In[11]:


# Subset arrests data
arrestdata = crime[crime.Arrest =="Success"]


# 2. What community area had the most arrests?

# In[12]:


# Read the community data
community = pd.read_csv("Community_area_list.csv")


# In[13]:


crime['Community Area'].describe()


# In[14]:


# merge community data with crime data
md = pd.merge(crime, community, left_on=['Community Area'], right_on= ['Community \nNumber'])


# In[15]:


md = md[['Primary Type','Community']]


# In[16]:


md


# In[17]:


most_arrests = pd.DataFrame(md['Community'].value_counts()[1:10])


# In[18]:


fig = plt.figure(figsize = (20,5))
most_arrests.plot(kind = 'bar',ax = plt.gca())


# In[19]:


most_arrests


# 'Near North Side', 'South Shore', 'North Lawndale', 'Near West Side',
#        'Humboldt Park', 'Auburn Gresham', 'Loop', 'West Englewood',
#        'West Town' has the most arrests

# 3.what crime caused most of the arrests? 

# In[20]:


most_crime = pd.DataFrame(md['Primary Type'].value_counts()[1:10])


# In[21]:


fig = plt.figure(figsize = (20,10))
most_crime.plot(kind = 'bar', title = 'Arrest by Crime Type', ax = plt.gca() )


# In[22]:


most_crime[1:10]


# In[23]:


most_crime.index[1:10]


# 'BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'OTHER OFFENSE', 'ASSAULT',  'DECEPTIVE PRACTICE', 'BURGLARY', 'MOTOR VEHICLE THEFT', 'ROBBERY' caused caused most of the arrests

# In[24]:


# Read the population data
population = pd.read_csv("Illinois_Population.csv")


# In[ ]:




