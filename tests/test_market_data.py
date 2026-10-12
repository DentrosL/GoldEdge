from datetime import datetime

from src.market_data import Candle

# Test for the Candle class
def test_create_candle():
    candle = Candle(
        timestamp=datetime(2026, 10, 11, 10, 0),
        open=4000.0,
        high=4010.0,
        low=3995.0,
        close=4005.0,
        volume=150,
    )

    assert candle.open == 4000.0
    assert candle.high == 4010.0
    assert candle.low == 3995.0
    assert candle.close == 4005.0
    assert candle.volume == 150