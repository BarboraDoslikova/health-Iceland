# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:43:20 2015

@author: Barbora Doslikova
"""

import scriptHealthIceland_functions

#reads in healthIceland.csv data with 3 columns and 49 rows:
# - 'Year' (for 49 years: 1964-2012)
# - 'Total accidents' (numbers are per 100,000 population)
# - 'Total accidents' (numbers are per 100,000 population)
data = scriptHealthIceland_functions.read_file()

# calculates the 4th column
data['% of fatal to total accidents'] = data['Total fatal accidents'] / data['Total accidents'] * 100
# 5thcolumn for weighting size of fatal accidents by total accidents
data['TA Weighted'] = (data['Total accidents']/300) * (data['Total accidents']/300)
# imaginary of acceprable no of fatal accidents
f_limit = 10
# 6th column to plot data above the limit
data['Above fatal limit'] =  data['Total fatal accidents'] > f_limit
# imaginary of acceprable no of total accidents
t_limit = 2500
# 7th column to plot data above the limit 
data['Above total limit'] =  data['Total accidents'] > t_limit


### PLOTTING ###
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# plots scatter graph of fatal accidents (by year) sized according to total accidens
data.plot(kind='scatter', x='Year', y='Total fatal accidents', s=data['TA Weighted'])
#data.plot(kind='scatter', x='Year', y='Total fatal accidents', c='Total accidents', s=data['TA Weighted'])

# if no of fatal accidents is above the selected f_limit, show black
data.plot(kind='scatter', x='Year', y='Total fatal accidents', c='Above fatal limit', s=data['TA Weighted'])

# if no of total accidents is above the selected t_limit, show black
data.plot(kind='scatter', x='Year', y='Total fatal accidents', c='Above total limit', s=data['TA Weighted'])

# but the figure needs an x axis label:


