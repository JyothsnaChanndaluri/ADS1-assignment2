# -*- coding: utf-8 -*-

# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""# Load the dataset"""

file_path = 'Climate Change in Romania from 1901-2020.xlsx'
data = pd.read_excel(file_path)

data.head()

data.tail()

data.info()

"""# Display basic statistics"""

print("Display basic statistics")
print(data.describe())

# Correlation matrix
correlation_matrix = data.corr()
print(correlation_matrix)

# Visualization 1: Boxplot of Annual Precipitation for different counties
plt.figure(figsize=(10, 6))
sns.boxplot(x='County/Country', y='Annual', data=data)
plt.title('Annual Precipitation for Counties')
plt.xticks(rotation=45)
plt.xlabel('County/Country')
plt.ylabel('Annual Precipitation')
plt.show()

# Visualization 2: Line plot for Monthly Precipitation for a specific county (e.g., Botosani)
county_data = data[data['County/Country'] == 'Botosani']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.figure(figsize=(10, 6))
plt.plot(months, county_data.iloc[0, 4:], marker='o')
plt.title('Monthly Precipitation in Botosani')
plt.xlabel('Month')
plt.ylabel('Precipitation')
plt.grid(True)
plt.show()

# Visualization 3: Heatmap showing correlations between variables
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

