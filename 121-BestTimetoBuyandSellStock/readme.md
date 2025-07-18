# 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the i<sup>th</sup> day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

## Example 1:
<pre>
Input: prices = [7,1,5,3,6,4]
Output: 5
</pre>
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

## Example 2:
<pre>
Input: prices = [7,6,4,3,1]
Output: 0
</pre>
Explanation: In this case, no transactions are done and the max profit = 0.
 
---
## Constraints:
<pre>
1 <= prices.length <= 10<sup>5</sup>
0 <= prices[i] <= 10<sup>4</sup>
</pre>