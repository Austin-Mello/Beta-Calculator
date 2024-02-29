import pandas as pd
from yahoo_fin.stock_info import get_data
from datetime import date, timedelta

print("Welcome to the beta calculator!")
t1 =str(input("Enter the ticker name of your first security:"))
t2 = str(input("Enter the ticker name of your second security:"))
#t1 = "AAPL"
#t2 = "SPY"

#Dataframe for the holdings
prices = pd.DataFrame()
rets = pd.DataFrame()

#Grab timestamps
end = date.today()
start = end - timedelta(days=365*2)

prices[t1] = get_data(t1, start_date=start, end_date=end).close
prices[t2] = get_data(t2, start_date=start, end_date=end).close
rets = prices.pct_change().dropna()
covariance = rets[t1].cov(rets[t2])
market_variance = rets[t2].var()
beta = covariance / market_variance

print(rets)
print("Covariance:", covariance)
print("Varience:", market_variance)
print(beta)