# Quick start

```sh
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install yfinance
git clone https://github.com/jintonic/finance
cd finance
python pair.py
deactivate
```

# Files

- [pair.py](pair.py): pair trading of SPY and QQQ. It draws z-score =: [(SPY-QQQ) - mean(60d)] / std(60d). If z>1, sell SPY, buy QQQ; If z<-1, sell QQQ, buy SPY; if z ~ 0, sell both to realize the profit. Sell and buy equal dollar amount to hedge risk.

# References
- <https://ranaroussi.github.io/yfinance/>
