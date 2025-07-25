# 28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

---

## Example 1:
<pre>
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
</pre>
Explanation: "sad" occurs at index 0 and 6.

The first occurrence is at index 0, so we return 0.


## Example 2:
<pre>
Input: haystack = "leetcode", needle = "leeto"
Output: -1
</pre>
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
---

## Constraints:
<pre>
1 <= haystack.length, needle.length <= 10<sup>4</sup>
haystack and needle consist of only lowercase English characters.
</pre>