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
# 5thcolumn for weighting size of plotter fat acc values
data['TA Weighted'] = (data['Total accidents']/300) * (data['Total accidents']/300)
# imaginary of acceprable no of fatal accidents
f_limit = 10
# 6th column too plot data above the limit 10
data['Above fatal limit'] =  data['Total fatal accidents'] > f_limit


### PLOTTING ###
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# if no of total accidents is above an arbitrary limit, make black
data.plot(kind='scatter', x='Year', y='Total fatal accidents', c='Above fatal limit', s=data['TA Weighted'])

# but the figure needs an x axis label:
