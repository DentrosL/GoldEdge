# GoldEdge

Algorithmic trading research and automation for XAUUSD (Gold) using Python and MetaTrader 5.

## About

GoldEdge is a personal project focused on developing and testing trading strategies for the gold market (XAUUSD).

The project aims to transform price action concepts into structured, testable rules, with an emphasis on market structure, trade triggers, and risk management.

Development takes place on Linux, while integration testing and execution are planned for Windows.

## Objectives

- Analyze historical market data.
- Identify price structures, including swing highs and swing lows.
- Define and evaluate trade entry and exit conditions.
- Implement position sizing and risk management rules.
- Test strategies using historical data before demo execution.
- Integrate with MetaTrader 5 for market data and trade execution.

## Tech Stack

- Python
- Pandas
- NumPy
- Pytest
- MetaTrader 5

## Project Structure

```
GoldEdge/
├── src/
│   ├── market_data.py
│   └── candle_reader.py
├── tests/
│   ├── test_market_data.py
│   └── test_candle_reader.py
├── data/
├── reports/
├── requirements.txt
└── README.md
```