# 238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

---

## Example 1:
<pre>
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
</pre>

## Example 2:
<pre>
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
</pre>

---

## Constraints:
<pre>
2 <= nums.length <= 10<sup>5</sup>
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
</pre>

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)