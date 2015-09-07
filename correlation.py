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

# Histograms:
import matplotlib
matplotlib.style.use('ggplot')
data.hist(bins=50)

# Tests:
import scipy as sc
print('Total accidents skewtest teststat = %6.3f pvalue = %6.4f' % sc.stats.skewtest(data['Total accidents']))
# => +1.6 = highly skewed to the left (+-0.5 = normal)
print('Total accidents kurtosis teststat = %6.3f pvalue = %6.4f' % sc.stats.kurtosistest(data['Total accidents']))
# => -2.6 = highly flatter than normal (0 = normal)(-3 = completely flat)
print('Total accidents normaltest teststat = %6.3f pvalue = %6.4f' % sc.stats.normaltest(data['Total accidents']))
# => skew & kurtosis tests combined, not normal if p is significant 

print('Total fatal accidents skewtest teststat = %6.3f pvalue = %6.4f' % sc.stats.skewtest(data['Total fatal accidents']))
print('Total fatal accidents kurtosis teststat = %6.3f pvalue = %6.4f' % sc.stats.kurtosistest(data['Total fatal accidents']))
print('Total fatal accidents normaltest teststat = %6.3f pvalue = %6.4f' % sc.stats.normaltest(data['Total fatal accidents']))

print('Year skewtest teststat = %6.3f pvalue = %6.4f' % sc.stats.skewtest(data['Year']))
print('Year kurtosis teststat = %6.3f pvalue = %6.4f' % sc.stats.kurtosistest(data['Year']))
print('Year normaltest teststat = %6.3f pvalue = %6.4f' % sc.stats.normaltest(data['Year']))

# Q-Q plots:
import pylab
import scipy.stats as stats

# as individual plots
stats.probplot(data['Total accidents'], dist="norm", plot=pylab)
pylab.show()
stats.probplot(data['Total fatal accidents'], dist="norm", plot=pylab)
pylab.show()
stats.probplot(data['Year'], dist="norm", plot=pylab)
pylab.show()

'''
# as subplots
import matplotlib.pyplot as plt
import scipy.stats as stats
ax1 = plt.subplot(311)
x = data['Total accidents']
res = stats.probplot(x, plot=plt)

ax2 = plt.subplot(312)
x = data['Total fatal accidents']
res = stats.probplot(x, plot=plt)

ax3 = plt.subplot(313)
x = data['Year']
res = stats.probplot(x, plot=plt)
'''

# Conclusion:
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
# => these two variables are negatively correlated
# i.e. the more total accidents the fewer fatal accidents
# => Fatal accidents have been going down inspite of growing no. of total accidents.

# Are the correlations significant?
cor1 = stats.spearmanr(data['Total accidents'], data['Year'])
print('Total accidents vs. Year: {0}'.format(cor1))
cor2 = stats.spearmanr(data['Total fatal accidents'], data['Year'])
print('Total fatal accidents vs. Year: {0}'.format(cor2))
cor3 = stats.spearmanr(data['Total fatal accidents'], data['Total accidents'])
print('Total fatal accidents vs. Total accidents: {0}'.format(cor3))
# => All three correlations are statistically significant
