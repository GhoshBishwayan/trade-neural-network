from pathlib import Path

root = Path(__file__).resolve().parent
parser_path = root / 'app' / 'parsers' / 'csv_parser.py'
req_path = root / 'requirements.txt'
data_dir = root / 'data'
sample_path = data_dir / 'sample.csv'

parser_text = '''from pathlib import Path

import pandas as pd
from app.models import Trade

REQUIRED_COLUMNS = {
    "symbol",
    "entry_time",
    "exit_time",
    "entry_price",
    "exit_price",
    "volume",
    "profit",
}


def parse_csv(file_path):
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError as exc:
        raise ValueError(f"CSV file is empty: {file_path}") from exc
    except (pd.errors.ParserError, UnicodeDecodeError) as exc:
        raise ValueError(f"Failed to read CSV file {file_path}: {exc}") from exc

    if df.empty:
        raise ValueError(f"CSV file contains no rows: {file_path}")

    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"CSV is missing required columns: {', '.join(sorted(missing_columns))}"
        )

    try:
        df["entry_time"] = pd.to_datetime(df["entry_time"], errors="raise")
        df["exit_time"] = pd.to_datetime(df["exit_time"], errors="raise")
    except (ValueError, TypeError) as exc:
        raise ValueError(f"Invalid timestamp in CSV data: {exc}") from exc

    trades = []
    for index, row in df.iterrows():
        try:
            trades.append(
                Trade(
                    symbol=str(row["symbol"]),
                    entry_time=row["entry_time"],
                    exit_time=row["exit_time"],
                    entry_price=float(row["entry_price"]),
                    exit_price=float(row["exit_price"]),
                    volume=float(row["volume"]),
                    profit=float(row["profit"]),
                )
            )
        except Exception as exc:
            raise ValueError(
                f"Malformed trade row at index {index}: {exc}"
            ) from exc

    return trades
'''

parser_path.write_text(parser_text, encoding='utf-8')

# Normalize requirements.txt to UTF-8 if encoded as UTF-16
req_bytes = req_path.read_bytes()
try:
    req_text = req_bytes.decode('utf-8')
except UnicodeDecodeError:
    req_text = req_bytes.decode('utf-16')
req_path.write_text(req_text, encoding='utf-8')

sample_data = '''symbol,entry_time,exit_time,entry_price,exit_price,volume,profit
AAPL,2025-01-02 09:30:00,2025-01-02 16:00:00,150.0,152.0,100,200.0
MSFT,2025-01-03 09:30:00,2025-01-03 16:00:00,250.0,248.0,50,-100.0
'''

data_dir.mkdir(exist_ok=True)
sample_path.write_text(sample_data, encoding='utf-8')

print('parser_written', parser_path.exists())
print('requirements_written', req_path.exists())
print('sample_written', sample_path.exists())
