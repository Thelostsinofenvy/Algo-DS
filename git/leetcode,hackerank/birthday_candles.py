from typing import ChainMap, Counter


candles = [4, 4, 1, 3]

# brute force


def birthdayCakeCandles(candles):
    high = []
    num = []
    # finding duplicate
    for i in range(0, len(candles)):
        for j in range(i+1, len(candles)):
            if candles[j] == candles[i]:
                high.append(candles[j])
                high.append(candles[i])
  # finding highest duplicate value
    candle = high.count(max(high))
    print(candle)


birthdayCakeCandles(candles)

# simple solution


def birthdayCakeCandles(candles):
    return candles.count(max(candles))
