#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# In[33]:


# Load the dataset
dataset = pd.read_csv("hw2.csv")


# In[34]:


# Extract the 'Flight Distance' column
flight_distance = dataset['Flight Distance'].values.reshape(-1, 1)


# In[35]:


# Min-max normalization
min_max_scaler = MinMaxScaler()
flight_distance_minmax = min_max_scaler.fit_transform(flight_distance)


# In[36]:


# Z-score normalization
z_score_scaler = StandardScaler()
flight_distance_zscore = z_score_scaler.fit_transform(flight_distance)


# In[37]:


# Replace the original column with the normalized values
dataset['Flight Distance (Min-Max)'] = flight_distance_minmax.flatten()
dataset['Flight Distance (Z-score)'] = flight_distance_zscore.flatten()


# In[38]:


# Print the updated dataset with normalized values
print(dataset.head())


# In[39]:


# Save the updated dataset
dataset.to_csv("HW2_normalized.csv", index=False)


# In[ ]:




