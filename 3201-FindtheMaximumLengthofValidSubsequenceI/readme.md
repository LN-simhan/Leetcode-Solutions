# 3201. Find the Maximum Length of Valid Subsequence I

You are given an integer array nums.

A subsequence sub of nums with length x is called valid if it satisfies:

<pre>(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.</pre>
Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

---

## Example 1:
<pre>
Input: nums = [1,2,3,4]

Output: 4
</pre>
Explanation:

The longest valid subsequence is [1, 2, 3, 4].

## Example 2:
<pre>
Input: nums = [1,2,1,1,2,1,2]

Output: 6
</pre>
Explanation:

The longest valid subsequence is [1, 2, 1, 2, 1, 2].

## Example 3:
<pre>
Input: nums = [1,3]

Output: 2
</pre>
Explanation:

The longest valid subsequence is [1, 3].

---

## Constraints:
<pre>
2 <= nums.length <= 2 * 10<sup>5</sup>
1 <= nums[i] <= 10<sup>7</sup>
</pre>