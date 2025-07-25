# 55. Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

---

## Example 1:
<pre>
Input: nums = [2,3,1,1,4]
Output: true
</pre>
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

## Example 2:
<pre>
Input: nums = [3,2,1,0,4]
Output: false
</pre>
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
---

## Constraints:
<pre>
1 <= nums.length <= 10<sup>4</sup>
0 <= nums[i] <= 10<sup>5</sup>
</pre>