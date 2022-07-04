from typing import List

"""
Question: 
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

BreakUp:

"""


class Solution:
    def max_profit_simple_approach(self, prices):
        profit = 0
        lowest_val = prices[0]
        highest_val = -1
        buy_day = 0
        sell_day = 0

        total_prices_len = len(prices) - 1

        if total_prices_len == 0:
            return 0

        for day, price in enumerate(prices):
            if buy_day > sell_day and highest_val != -1:
                highest_val = -1

            if lowest_val > price and day != total_prices_len:
                lowest_val = price
                buy_day = day

            if day > buy_day and highest_val <= price:
                highest_val = price
                sell_day = day
                temp_profit = highest_val - lowest_val

                if temp_profit > profit:
                    profit = temp_profit

        return profit

    def max_profit(self, prices: List[int]) -> int:
        profit = 0
        return profit


if __name__ == "__main__":
    solution_obj = Solution()
    print(solution_obj.max_profit_simple_approach(prices=[7, 1, 5, 3, 6, 4]))  # Expected 5
    print(solution_obj.max_profit_simple_approach(prices=[2, 4, 1]))  # Expected 2
    print(solution_obj.max_profit_simple_approach(prices=[1, 2]))  # Expected 1
    print(solution_obj.max_profit_simple_approach(prices=[2, 1, 2, 1, 0, 1, 2]))  # Expected 2
    print(solution_obj.max_profit_simple_approach(prices=[3, 3, 5, 0, 0, 3, 1, 4]))  # Expected 4
    print(solution_obj.max_profit_simple_approach(prices=[3, 2, 6, 5, 0, 3]))  # Expected 4
