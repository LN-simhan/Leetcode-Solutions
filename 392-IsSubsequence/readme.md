# 392. Is Subsequence

Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>s</code> is a <b>subsequence</b> of <code>t</code>, or <code>false</code> otherwise.

A <b>subsequence</b> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>"ace"</code> is a subsequence of <code>"abcde"</code> while <code>"aec"</code> is not).

---

## Example 1:
<pre>
Input: s = "abc", t = "ahbgdc"
Output: true
</pre>

## Example 2:
<pre>
Input: s = "axc", t = "ahbgdc"
Output: false
</pre>

---

## Constraints:
<pre>
0 <= s.length <= 100
0 <= t.length <= 10<sup>4</sup>
s and t consist only of lowercase English letters.
</pre>

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10<sup>9</sup>, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?