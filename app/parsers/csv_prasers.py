import pandas as pd
from app.models import Trade

def parse_csv(file_path):
    df = pd.read_csv(file_path)

    trades = []

    for _, row in df.iterrows():
        trades.append(
            Trade(
                symbol=row["symbol"],
                entry_time=row["entry_time"],
                exit_time=row["exit_time"],
                entry_price=row["entry_price"],
                exit_price=row["exit_price"],
                volume=row["volume"],
                profit=row["profit"]
            )
        )

    return trades