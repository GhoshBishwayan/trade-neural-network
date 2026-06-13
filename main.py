import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app.parsers.csv_parser import parse_csv
from app.analytics.basic import (
    calculate_win_rate,
    calculate_profit_factor,
    calculate_best_symbol,
    calculate_best_day,
)

DATA_FILE = ROOT_DIR / "data" / "sample.csv"

try:
    trades = parse_csv(DATA_FILE)
except Exception as exc:
    raise SystemExit(f"Failed to load trades from {DATA_FILE}: {exc}") from exc

print("Win Rate:", calculate_win_rate(trades), "%")
print("Profit Factor:", calculate_profit_factor(trades))
print("Best Symbol:", calculate_best_symbol(trades))
print("Best Day:", calculate_best_day(trades))