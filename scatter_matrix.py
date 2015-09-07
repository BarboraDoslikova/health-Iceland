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
# imaginary of acceprable no of total accidents
t_limit = 2500
# 7th column too plot data above the limit 2000
data['Above total limit'] =  data['Total accidents'] > t_limit

######################################################
# To display 4 colours, showing data above both limits
######################################################

colour_1 = 'above both limits'
colour_2 = 'above fatal limit'
colour_3 = 'above total limit'
colour_4 = 'passed' 

def my_function(row):
    if (row['Above fatal limit'] == True & row['Above total limit'] == True):
        return colour_1
    if row['Above fatal limit'] == True:
        return colour_2
    if row['Above total limit'] == True:
        return colour_3
    else:
        return colour_4

# make a colmun with 1 of 4 groups
data['Groups'] = data.apply(my_function, axis=1)

# extracts unnecessary columns for scatter matrix 
data2 = data.drop('TA Weighted', 1)
data3 = data2.drop('Above fatal limit', 1)
data4 = data3.drop('Above total limit', 1)
data5 = data4.drop('% of fatal to total accidents', 1)

# plot scatter matrix
import seaborn as sns

sns.set()
sns.set_context("paper") # not talk, poster, notebook
sns.pairplot(data5, hue="Groups", diag_kind="hist")

'''
# save the plot
from pylab import savefig
savefig('scatter_matrix.png', dpi = 150)
'''
