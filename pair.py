# https://ranaroussi.github.io/yfinance
import yfinance as yf

spy = yf.Ticker("SPY").history('25y', interval='1wk')
qqq = yf.Ticker("QQQ").history('25y', interval='1wk')

spread = spy['Close'] - qqq['Close']

# https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html
mean = spread.rolling(60, min_periods=1).mean()
std = spread.rolling(60, min_periods=1).std()

score = (spread-mean)/std

# https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.html
axes = score.plot(figsize=(14,4))
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axhline.html
axes.axhline(y=1, ls="-.")
axes.axhline(y=-1, ls="-.")

import matplotlib.pyplot as plt
plt.grid()
plt.ylim(-6, 6)
plt.show()
