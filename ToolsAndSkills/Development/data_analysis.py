#
# This is a Python Script
# for Financial Data Analysis
#

import pandas as pd

url = 'http://hilpisch.com/tr_eikon_eod_data.csv'

data = pd.read_csv(url, index_col=0, parse_dates=True)

if __name__ == '__main__':
    print(data.info())
