# 45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
<pre>
<li>0 <= j <= nums[i] and
<li>i + j < n
</pre>
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

--- 

## Example 1:
<pre>
Input: nums = [2,3,1,1,4]
Output: 2
</pre>
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

## Example 2:
<pre>
Input: nums = [2,3,0,1,4]
Output: 2
</pre>

## Constraints:
<pre>
1 <= nums.length <= 10<sup>4</sup>
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
</pre>