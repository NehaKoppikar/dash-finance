import pandas_datareader as data
import pandas as pd

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
#tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2020-01-01'
end_date = '2021-01-16'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader('INPX', 'yahoo', start_date, end_date)

panel_data.to_csv("data.csv")

