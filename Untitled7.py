#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the water quality dataset
cancer_dataset = pd.read_csv("C:/Users/USER/Desktop/New folder/cancer/cancer patient data sets.csv")

# Print the first 5 rows of the dataset
cancer_dataset.head()


# In[3]:


# check if there are null values in the datasets
cancer_dataset.isnull().sum()


# In[4]:


# give a full description of your dataset
cancer_dataset.describe()


# In[8]:


# visualise the distribution of the numerical value with respect to Potability
columns=cancer_dataset.select_dtypes(exclude="object").columns
for i in range(len(columns)-1):
    plt.figure(figsize=(8,5))
    sns.histplot(data=cancer_dataset, x=cancer_dataset[columns[i]], kde=True, color="red")
    plt.title({columns[i]})
    plt.show()


# In[ ]:


sulfate = dataset['Sulfate']
conductivity = dataset['Conductivity']


# Create subplots
plt.figure(figsize=(10, 5))  # Adjust the figure size as needed
plt.subplot(2, 2, 1)  # Create the first subplot
plt.hist(pH, bins=20, color='blue', alpha=0.5, label='pH')  # Customize the histogram
plt.xlabel('X-axis Label')
plt.ylabel('Frequency')
plt.title('Histogram of pH')
plt.legend()

plt.subplot(2, 2, 2)  # Create the second subplot
plt.hist(hardness, bins=20, color='red', alpha=0.5, label='hardness')  # Customize the histogram
plt.xlabel('X-axis Label')
plt.ylabel('Frequency')
plt.title('Histogram of hardness')
plt.legend()

plt.subplot(2, 2, 3)  # Create the third subplot
plt.hist(solids, bins=20, color='green', alpha=0.5, label='solids')  # Customize the histogram
plt.xlabel('X-axis Label')
plt.ylabel('Frequency')
plt.title('Histogram of solids')
plt.legend()

plt.subplot(2, 2, 4)  # Create the fourth subplot
plt.hist(chloramines, bins=20, color='purple', alpha=0.5, label='chloramines')  # Customize the histogram
plt.xlabel('X-axis Label')
plt.ylabel('Frequency')
plt.title('Histogram of chloramines')
plt.legend()


# Show the plot
plt.tight_layout()  # Ensures subplots do not overlap
plt.show()

