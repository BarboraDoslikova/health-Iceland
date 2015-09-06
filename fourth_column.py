# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:43:20 2015

@author: BD
"""

import scriptHealthIceland_functions

#reads in healthIceland.csv data with 3 columns and 49 rows:
# - 'Year' (for 49 years: 1964-2012)
# - 'Total accidents' (numbers are per 100,000 population)
# - 'Total accidents' (numbers are per 100,000 population)
data = scriptHealthIceland_functions.read_file()

# calculates the 4th column
data['% of fatal to total accidents'] = data['Total fatal accidents'] / data['Total accidents'] * 100
