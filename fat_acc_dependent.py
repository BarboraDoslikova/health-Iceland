# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:43:20 2015

@author: lenovo
"""

import scriptHealthIceland_functions

#reads in healthIceland.csv data with 3 columns and 49 rows:
# - 'Year' (for 49 years: 1964-2012)
# - 'Total accidents' (numbers are per 100,000 population)
# - 'Total accidents' (numbers are per 100,000 population)
data = scriptHealthIceland_functions.read_file()

# 5th column for the weighting of total fatal accidents by total accidents
data['TA Weighted'] = (data['Total accidents']/300) * (data['Total accidents']/300)

### PLOTTING ###
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# No. of total fatal accidents has decreased over time...
data.plot(kind='scatter', x='Year', y='Total fatal accidents', s=50)
# ...seemingly independently of total accidents.
data.plot(kind='scatter', x='Year', y='Total fatal accidents', s=data['TA Weighted'])
data.plot(kind='scatter', x='Year', y='Total fatal accidents', c='Total accidents', s=data['TA Weighted'])

# Is this as a result of decreased no. of total accidents?
data.plot(kind='scatter', x='Total accidents', y='Total fatal accidents')

# linear regression shows a RS btw fatal accidents and total accidents
# i.e. fewer fatal accidents with fewer total accidents
import seaborn as sns
sns.lmplot(x="Total accidents", y="Total fatal accidents", data=data);
# => No. of fatal accidents has decreased independently of no. of total accidents
