#한번의 거래로 낼 수 있는 최대 이익을 산출하라
import sys

from pip._internal.utils.misc import enum

def maxProfit(prices):

    min_price = sys.maxsize
    max_profit = 0

    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]

print(maxProfit(prices))