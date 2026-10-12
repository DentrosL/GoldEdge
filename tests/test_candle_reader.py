from pathlib import Path

from src.candle_reader import read_candles

# test 2 
def test_read_candles():
    file_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "sample_candles.csv"
    )

    candles = read_candles(str(file_path))

    assert len(candles) == 5
    assert candles.iloc[0]["open"] == 3980.0
    assert candles.iloc[0]["close"] == 3987.0
    assert candles["timestamp"].notna().all()