import pandas as pd

REQUIRED_COLUMNS = [
    "timestamp",
    "open",
    "high",
    "low",
    "close",
    "volume",
]

def read_candles(file_path: str) -> pd.DataFrame:
    candles = pd.read_csv(file_path)

    missing_columns = set(REQUIRED_COLUMNS) - set(candles.columns)

    if missing_columns:
        raise ValueError(
            f"Colunas ausentes no arquivo: {sorted(missing_columns)}"
        )

    candles["timestamp"] = pd.to_datetime(
        candles["timestamp"],
        errors="raise",
    )

    return candles