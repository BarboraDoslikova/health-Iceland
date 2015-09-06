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

# calculates the 4th column
data['% of fatal to total accidents'] = data['Total fatal accidents'] / data['Total accidents'] * 100

''' For dropping 'Year' column
# extracts years
years = data['Year']
# data frame without the 1st/'Year' column
data2 = data.drop('Year', 1)
'''

### PLOTTING ###
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# plots scatter graph of Year vs. fatal accidents
data.plot(kind='scatter', x='Year', y='Total accidents')

# plots scatter graph of Year vs. fatal accidents
data.plot(kind='scatter', x='Year', y='Total fatal accidents')

# plots scatter graph of Year vs. %
data.plot(kind='scatter', x='Year', y='% of fatal to total accidents')

# scatter plot:
# No of fatal accidents has decreased independently of no of total accidents.
data.plot(kind='scatter', x='Total accidents', y='Total fatal accidents')
