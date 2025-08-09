import yfinance as yf

SPY = yf.Ticker("SPY")
QQQ = yf.Ticker("QQQ")

spy = SPY.history(period='1y')
qqq = QQQ.history(period='1y')

dif = spy['Close'] - qqq['Close']

mean = dif.tail(60).mean()
std = dif.tail(60).std()

score = (dif-mean)/std
score.plot()

import matplotlib.pyplot as plt

plt.show()
