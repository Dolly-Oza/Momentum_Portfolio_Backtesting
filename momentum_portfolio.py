import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assets

tickers = {
    "HDFCBANK": "HDFCBANK.NS",
    "RELIANCE": "RELIANCE.NS",
    "HINDZINC": "HINDZINC.NS",
    "NIFTY50": "^NSEI"
}

start_date = "2018-01-01"
momentum_window = 60

# Downloading Price Data

price_data = pd.DataFrame()

for name, ticker in tickers.items():
    data = yf.download(ticker, start=start_date, auto_adjust=True)
    price_data[name] = data["Close"]


# Returns & Momentum
returns = price_data.pct_change(fill_method=None)
momentum = returns.rolling(momentum_window).sum()

# Rebalancing (monthly)

monthly_momentum = momentum.resample("ME").last()
monthly_returns = returns.resample("ME").sum()

# Ranking Assets

ranks = monthly_momentum.rank(axis=1, ascending=False)

# Top 4 assets and Equal weights allocated
top_n = 4
signals = (ranks <= top_n).astype(int)
weights = signals.div(signals.sum(axis=1), axis=0)

# Shift to avoid look-ahead bias
portfolio_returns = (weights.shift(1) * monthly_returns).sum(axis=1)

# Performance

portfolio_cum = (1 + portfolio_returns).cumprod()
market_cum = (1 + monthly_returns["NIFTY50"]).cumprod()

# Plotting

plt.figure(figsize=(10, 5))
plt.plot(portfolio_cum, label="Momentum Portfolio")
plt.plot(market_cum, label="NIFTY 50 Buy & Hold")
plt.legend()
plt.title("Momentum Portfolio vs NIFTY 50")
plt.show()

# Sharpe Ratio (annualized) and Maximum Drawdown

sharpe_ratio = (portfolio_returns.mean() / portfolio_returns.std()) * np.sqrt(12)

rolling_max = portfolio_cum.cummax()
drawdown = (portfolio_cum - rolling_max) / rolling_max
max_drawdown = drawdown.min()

print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")