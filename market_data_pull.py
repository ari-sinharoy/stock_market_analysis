'''
Pull historical global market data
'''

import pandas as pd
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2014,1,2)
end = datetime.date.today()

# we will study and compare the following 4 market indices
markets = ["bse","s&p500","sse","crude_oil"]
market_ind = ["^BSESN","^GSPC","000001.SS","CL=F"]

market_dict = {}
for item in range(len(markets)):
    df = web.DataReader(market_ind[item],'yahoo',start,end)
    market_dict.update({markets[item]:df["Adj Close"]})

# collect historical market data in a dataframe    
market_df = pd.DataFrame(market_dict)

# data preprocessing
print(f"Fraction of missing data\n{market_df.isna().sum()/len(market_df)}")

# use interpolation method for missing data
market_dfi = market_df.interpolate()

# plot the historical data 
dat_df = market_dfi.copy()
dat_df /= dat_df.max()
dat_df.plot(grid=True)

# sace the data in a csv file
f_path = r"C:\Users\JJ\Desktop\Data Science Projects\Share_Market_Trends"
market_dfi.to_csv(f_path + '\hist.csv', index = False, header=True)