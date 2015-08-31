# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:02:28 2015

@author: Barbora Doslikova

Demonstrates how data from healthIceland.csv can be read using 2 methods:
(A) 16 lines of code: returns a list of integers
(B) 2 lines of code: returns a pandas DataFrame. 

healthIceland.csv has 3 columns and 49 rows:
- 'Year' (for 49 years: 1964-2012)
- 'Total accidents' (numbers are per 100,000 population)
- 'Total accidents' (numbers are per 100,000 population)

Data are downloadable from 'http://www.statice.is/?PageID=1282&src=https://rannsokn.hagstofa.is/pxen/Dialog/varval.asp?ma=HEI12001%26ti=Accidents+reported+to+the+State+Social+Security+Institute+1964-2012++%26path=../Database/heilbrigdismal/slys/%26lang=1%26units=Number'
Select all years from the 'Year' colun 
and 'Total accidents' and 'Total fatal accidents' from the 'Accident' column.
"""

import pandas as pd

# OPTION A ###################################
##############################################

# opens csv file in read ("r") mode
f = open("healthIceland.csv", "r")

#string
data = f.read()

# list of strings; 
# but each row is 1 string instead of 3 integers
# and has an extra emptry strings at the end
# and a missing label for the 'Year' column
rows = data.split("\n") 

# converts data in each row into separate strings
# but each row is 3 strings instead of 3 integers
# and sill has an extra emptry strings at the end
# and a missing label for the 'Year' column
list_of_strings = []
for row in rows:
    split_row = row.split(",")
    list_of_strings.append(split_row)

# removes the first row of labels and the last empty row
# but each row is 3 strings instead of 3 integers   
length_list_of_strings = len(list_of_strings)-1
clean_list_of_strings = list_of_strings[1:length_list_of_strings]

# converts all strings to integers
# returns a list of 49 lists, each with 3 integers
list_of_integers = []
for inner_list in clean_list_of_strings:
    new_inner_list = []
    for item in inner_list:
        item_int = int(item)
        new_inner_list.append(item_int)      
    list_of_integers.append(new_inner_list) 

data = list_of_integers

print(data)

# returns error if not 49 rows present
assert len(data) == 49

# OPTION B ###################################
##############################################

# open data direcly as pandas.core.frame.DataFrame
df = pd.read_csv('healthIceland.csv')
# assign the proper column name 'Year' to the 1st column 
df.columns = ['Year', 'Total accidents', 'Total fatal accidents']

print(df)

# number of rows (49) by columns (3)
print(df.shape)
