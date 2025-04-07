import pandas as pd

class TechnicalIndicators:
    def __init__(self, dataframe):
        self.df = dataframe

    def add_ichimoku(self):
        high = self.df['High']
        low = self.df['Low']
        close = self.df['Close']

        self.df['Tenkan_Sen'] = (high.rolling(window=9).max() + low.rolling(window=9).min()) / 2
        self.df['Kijun_Sen'] = (high.rolling(window=26).max() + low.rolling(window=26).min()) / 2
        self.df['Senkou_Span_A'] = ((self.df['Tenkan_Sen'] + self.df['Kijun_Sen']) / 2).shift(26)
        self.df['Senkou_Span_B'] = ((high.rolling(window=52).max() + low.rolling(window=52).min()) / 2).shift(26)
        self.df['Chikou_Span'] = close.shift(-26)

    def add_macd(self, fast_period=12, slow_period=26, signal_period=9):
        close = self.df['Close']
        self.df['EMA_Fast'] = close.ewm(span=fast_period, adjust=False).mean()
        self.df['EMA_Slow'] = close.ewm(span=slow_period, adjust=False).mean()
        self.df['MACD'] = self.df['EMA_Fast'] - self.df['EMA_Slow']
        self.df['MACD_Signal'] = self.df['MACD'].ewm(span=signal_period, adjust=False).mean()

    def add_stochastics(self, k_period=14, d_period=3):
        high = self.df['High']
        low = self.df['Low']
        close = self.df['Close']
        self.df['Lowest_Low'] = low.rolling(window=k_period).min()
        self.df['Highest_High'] = high.rolling(window=k_period).max()
        self.df['%K'] = 100 * ((close - self.df['Lowest_Low']) / (self.df['Highest_High'] - self.df['Lowest_Low']))
        self.df['%D'] = self.df['%K'].rolling(window=d_period).mean()

    def add_bollinger_bands(self, period=20, std_dev=2):
        close = self.df['Close']
        self.df['BB_Middle'] = close.rolling(window=period).mean()
        self.df['BB_Upper'] = self.df['BB_Middle'] + (close.rolling(window=period).std() * std_dev)
        self.df['BB_Lower'] = self.df['BB_Middle'] - (close.rolling(window=period).std() * std_dev)

    
    def calculate_all_indicators(self):
        """
        Calculate and add all indicators to the DataFrame.
        """
        self.add_ichimoku()
        self.add_macd()
        self.add_stochastics()
        self.add_bollinger_bands()

# Example usage:
# df = pd.DataFrame({
#     'High': [...],
#     'Low': [...],
#     'Close': [...]
# })
# indicators = TechnicalIndicators(df)
# indicators.calculate_all_indicators()
# print(indicators.df)
