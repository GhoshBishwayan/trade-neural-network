from collections import Counter
from datetime import datetime

def calculate_win_rate(trades):
    if not trades:
        return 0

    wins = sum(1 for trade in trades if trade.profit > 0)

    return round((wins / len(trades)) * 100, 2)


def calculate_profit_factor(trades):
    gross_profit = sum(trade.profit for trade in trades if trade.profit > 0)

    gross_loss = abs(
        sum(trade.profit for trade in trades if trade.profit < 0)
    )

    if gross_loss == 0:
        return float("inf")

    return round(gross_profit / gross_loss, 2)


def calculate_best_symbol(trades):
    symbol_profit = {}

    for trade in trades:
        symbol_profit.setdefault(trade.symbol, 0)
        symbol_profit[trade.symbol] += trade.profit

    if not symbol_profit:
        return None

    return max(symbol_profit, key=symbol_profit.get)


def calculate_best_day(trades):
    day_profit = {}

    for trade in trades:
        day = trade.entry_time.strftime("%A")

        day_profit.setdefault(day, 0)
        day_profit[day] += trade.profit

    if not day_profit:
        return None

    return max(day_profit, key=day_profit.get)