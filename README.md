# Rolling Momentum Portfolio Backtesting
## About This Project

This project implements a rolling momentum-based portfolio strategy using selected Indian stocks and compares it with the NIFTY 50 index.

Strategy based on the fact that assets that performed well in the recent past may continue to perform well in the near future.

The portfolio is rebalanced monthly based on momentum rankings.

## Assets Used

HDFCBANK

RELIANCE

HINDZINC

NIFTY 50 (Benchmark)

Data Source: Yahoo Finance

Start Date: January 2018

## Strategy Overview

Download daily adjusted closing prices.

Calculate daily returns.

Compute 60-day rolling momentum (sum of returns).

Convert data to monthly frequency.

Rank assets based on monthly momentum.

Select top 4 assets.

Allocate equal weight to selected assets.

Rebalance monthly.

Shift weights by one month to avoid look-ahead bias.

## Backtest Results

**Sharpe Ratio (Annualized): 0.87**

**Maximum Drawdown: -29.41%**

Strategy compared against NIFTY 50 Buy & Hold

Equity curve plotted using Matplotlib

## How it works?

Follows momentum signal

Allocates capital equally among top-ranked assets

Rebalances monthly

Measures risk using Sharpe Ratio and Maximum Drawdown

## Assumptions

No transaction costs

Equal-weight allocation

Limited asset universe (4 assets)

## Libraries Used

Python

pandas

numpy

yfinance

matplotlib

## How to Run
pip install yfinance pandas numpy matplotlib

python rolling_momentum_portfolio.py
