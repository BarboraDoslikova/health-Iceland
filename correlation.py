# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:43:20 2015

@author: Barbora Doslikova
"""
######################## READ DATA ##########################
# reads in healthIceland.csv data with 3 columns and 49 rows:
# - 'Year' (for 49 years: 1964-2012)
# - 'Total accidents' (numbers are per 100,000 population)
# - 'Total accidents' (numbers are per 100,000 population)
import scriptHealthIceland_functions
data = scriptHealthIceland_functions.read_file()


######################## BASIC STATS ########################
decriptive = data.describe()
print(decriptive)


######################## NORMALLY DISTRIBUTED? ##############
import scipy as sc

# histograms
import matplotlib
matplotlib.style.use('ggplot')
data.hist(bins=50)

# tests
print('total skewtest teststat = %6.3f pvalue = %6.4f' % sc.stats.skewtest(data['Total accidents']))
# => +1.6 = highly skewed to the left (+-0.5 = normal)
print('total kurtosis teststat = %6.3f pvalue = %6.4f' % sc.stats.kurtosistest(data['Total accidents']))
# => -2.6 = highly flatter than normal (0 = normal)(-3 = completely flat)
print('total normaltest teststat = %6.3f pvalue = %6.4f' % sc.stats.normaltest(data['Total accidents']))
# => skew & kurtosis tests combined, not normal if p is significant 

print('fatal skewtest teststat = %6.3f pvalue = %6.4f' % sc.stats.skewtest(data['Total fatal accidents']))
print('fatal kurtosis teststat = %6.3f pvalue = %6.4f' % sc.stats.kurtosistest(data['Total fatal accidents']))
print('fatal normaltest teststat = %6.3f pvalue = %6.4f' % sc.stats.normaltest(data['Total fatal accidents']))

print('year skewtest teststat = %6.3f pvalue = %6.4f' % sc.stats.skewtest(data['Year']))
print('year kurtosis teststat = %6.3f pvalue = %6.4f' % sc.stats.kurtosistest(data['Year']))
print('year normaltest teststat = %6.3f pvalue = %6.4f' % sc.stats.normaltest(data['Year']))
# => none of the data are normally distributed, therefore use spearman (not pearson) correlation


######################## SPEARMAN CORRELATIONS ##############
# correlations table
correlations = data.corr(method='spearman')
print(correlations)

# visual representation of correlation matrix
correlations.plot(kind='bar') 

# OR single correlation value of the total fatal accidents vs. total accidents
correlations_spear = data['Total fatal accidents'].corr(data['Total accidents'], method='spearman')
print(correlations_spear)
# => the variables are moderately negatively correlated
# i.e. the more total accidents the fewer fatal accidents
# => Fatal accidents have been going down inspite of growing no. of total accidents.
