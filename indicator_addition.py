from packages.Technical import TechnicalIndicators
import pandas as pd

df = pd. read_csv('Data/coffee_futures_minute_data.csv', index_col=0, parse_dates=True)
indicators = TechnicalIndicators(df)
indicators.calculate_all_indicators()
indicators.df.to_csv('/Users/alexkoutromanos/Documents/GitHub/Coffee-Commodities/Data/indicators.csv')