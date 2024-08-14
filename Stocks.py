import pandas_datareader as pdr

# Define the stock exchange (e.g. NYSE, NASDAQ, etc.)
exchange = "NYSE"

# Get the top 10 stocks by market capitalization
top_stocks = pdr.get_data_yahoo(exchange, start="2022-01-01", end="2024-01-01")['MarketCap'].nlargest(10)

# Print the top 10 stocks
print(top_stocks)