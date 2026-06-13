import os
from app.parsers.csv_parser import parse_csv
from app.analytics.basic import *

trades = parse_csv("data/sample.csv")

print("Win Rate:", calculate_win_rate(trades), "%")
print("Profit Factor:", calculate_profit_factor(trades))
print("Best Symbol:", calculate_best_symbol(trades))
print("Best Day:", calculate_best_day(trades))