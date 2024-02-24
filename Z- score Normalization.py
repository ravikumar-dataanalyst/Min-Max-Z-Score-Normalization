#!/usr/bin/env python
# coding: utf-8

# # Case 1: Two fields correlation score is between 0-1

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


# Sample dataset
data = {
    'field1': [1, 2, 3, 4, 5],
    'field2': [2, 4, 6, 8, 10]
}

# Create a DataFrame from the sample dataset
df = pd.DataFrame(data)

# Calculate the correlation coefficient between 'field1' and 'field2'
correlation_coefficient = df['field1'].corr(df['field2'])

print("Correlation coefficient between 'field1' and 'field2':", correlation_coefficient)
#plot
plt.scatter(df['field1'], df['field2'])
plt.title('linear positive Correlation of field1 vs field2')
plt.xlabel('field1')
plt.ylabel('field2')
plt.show()


# # Explanation:  As per taken fields1 Vs fields 2, A positive correlation coefficient between 0 and 1 suggests that there is a linear relationship between the two variables, and as one variable increases, the other variable tends to increase as well. However, it's important to note that the strength of the correlation increases as the value of r approaches 1.

# # Case 2: Two fields correlation score is between 0 and -1

# In[12]:


import pandas as pd

# Sample dataset
data = {
    'field1': [1, 2, 3, 4, 5],
    'field2': [5, 4, 3, 2, 1]
}

# Create a DataFrame from the sample dataset
df = pd.DataFrame(data)

# Calculate the correlation coefficient between 'field1' and 'field2'
correlation_coefficient = df['field1'].corr(df['field2'])

print("Correlation coefficient between 'field1' and 'field2':", correlation_coefficient)
plt.scatter(df['field1'], df['field2'])
plt.title('linear Negative Correlation of field1 vs field2')
plt.xlabel('field1')
plt.ylabel('field2')
plt.show()


# # Explanation: As per taken fields1 Vs fields 2,A negative correlation coefficient between 0 and -1 suggests that there is a linear relationship between the two variables, and as one variable increases, the other variable tends to decrease. However, it's important to note that the strength of the correlation increases as the value of r approaches -1.

# # case 3: Two fields correlation score is Zero

# In[13]:


import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(0)

# Generate random values for 'field1' and 'field2'
n_samples = 50  # Number of samples
field1 = np.random.rand(n_samples)  # Random values for 'field1'
field2 = np.random.rand(n_samples)  # Random values for 'field2'

# Create a DataFrame from the generated data
df = pd.DataFrame({'field1': field1, 'field2': field2})

# Calculate the correlation coefficient between 'field1' and 'field2'
correlation_coefficient = df['field1'].corr(df['field2'])

print("Correlation coefficient between 'field1' and 'field2':", correlation_coefficient)
plt.scatter(df['field1'], df['field2'])
plt.title('No Correlation of field1 vs field2')
plt.xlabel('field1')
plt.ylabel('field2')
plt.show()


# # Explanation: As per taken fields1 Vs fields 2,Since the values for 'field1' and 'field2' are randomly generated and have no relationship between them, the correlation coefficient will be close to zero, indicating no correlation.

# # one More Case
# 

# In[15]:


import pandas as pd

# Sample dataset
data = {
    'field1': [1, 22, 3, 14, 51],
    'field2': [16, 2, 18, 32, 10]
}

# Create a DataFrame from the sample dataset
df = pd.DataFrame(data)

# Calculate the correlation coefficient between 'field1' and 'field2'
correlation_coefficient = df['field1'].corr(df['field2'])

print("Correlation coefficient between 'field1' and 'field2':", correlation_coefficient)
plt.scatter(df['field1'], df['field2'])
plt.title('No Correlation of field1 vs field2')
plt.xlabel('field1')
plt.ylabel('field2')
plt.show()


# # Explanation: The value of 0 for the Pearson correlation coefficient suggests that there is no linear association between the two variables. In other words, changes in one variable do not correspond to systematic changes in the other variable in a linear fashion.
