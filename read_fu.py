# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:02:28 2015

@author: Barbora Doslikova

Reads in data healthIceland.csv data.
Returns a data frame.

healthIceland.csv has 3 columns and 49 rows:
- 'Year' (for 49 years: 1964-2012)
- 'Total accidents' (numbers are per 100,000 population)
- 'Total accidents' (numbers are per 100,000 population)

Data are downloadable from 'http://www.statice.is/?PageID=1282&src=https://rannsokn.hagstofa.is/pxen/Dialog/varval.asp?ma=HEI12001%26ti=Accidents+reported+to+the+State+Social+Security+Institute+1964-2012++%26path=../Database/heilbrigdismal/slys/%26lang=1%26units=Number'
Select all years from the 'Year' colun 
and 'Total accidents' and 'Total fatal accidents' from the 'Accident' column.
"""

import pandas as pd

def read_file(name='healthIceland.csv'):
    # open data direcly as pandas.core.frame.DataFrame
    df = pd.read_csv(name)
    # assign the proper column name 'Year' to the 1st column 
    df.columns = ['Year', 'Total accidents', 'Total fatal accidents']
    return df

if __name__ == '__main__': # doesn't run if imported
    data = read_file()
    print(data)
