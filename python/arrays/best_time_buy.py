"""
You are given an array prices where prices[i]
is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1)
and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1
is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

from typing import List  # conform to legacy challenge interpreter < Python 3.9


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        2 variables corresponding to index 0/1 initially
        will traverse array based on nested 'j' two pointer technique - traversal is O(n^2)
        Challenge coditions state len >= 1, so checking for this case as well

        UPDATE: LeetCode passes but exceeds time limit. Refactoring 'while' for O(n) traversal
        """
        if len(prices) <= 1:
            return 0

        max_prof = 0  # To hold current difference of r_ptr - l_ptr.
        # Compared against max for loop 'profit' var

        # for i in range(len(prices)):
        # for j in range(i + 1, len(prices)):
        # if prices[i] < prices[j]:
        l_ptr, r_ptr = 0, 1
        while r_ptr < len(prices):
            if prices[l_ptr] < prices[r_ptr]:
                curr_profit = prices[r_ptr] - prices[l_ptr]
                # curr_profit = prices[j] - prices[i]
                max_prof = max(max_prof, curr_profit)
            else:
                l_ptr = r_ptr  # Move left ptr all the way over - j is low, so it's the curr best buy point
                # i = j
            r_ptr += 1  # Right ptr keeps moving at const rate each iteration regardless
        return max_prof  # If max(max_prof, curr_prof) eval negative diff, we still get desired zero


x = Solution
print(x.maxProfit(x, [7, 1, 5, 3, 6, 4]))
print(x.maxProfit(x, [7, 6, 4, 3, 1]))
print(x.maxProfit(x, []))
print(x.maxProfit(x, [1, 2]))
print(x.maxProfit(x, [2, 1]))
print(x.maxProfit(x, [1, 4, 2]))
print(x.maxProfit(x, [1, 6, 5, 1]))
print(x.maxProfit(x, [2, 4, 1]))
print(x.maxProfit(x, [2, 1, 2, 0, 1]))
