# 125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string <code>s</code>, return <code>true</code> if it is a palindrome, or <code>false</code> otherwise.

---

## Example 1:
<pre>
Input: s = "A man, a plan, a canal: Panama"
Output: true
</pre>
Explanation: "amanaplanacanalpanama" is a palindrome.


## Example 2:
<pre>
Input: s = "race a car"
Output: false
</pre>
Explanation: "raceacar" is not a palindrome.


## Example 3:
<pre>
Input: s = " "
Output: true
</pre>
Explanation: s is an empty string "" after removing non-alphanumeric characters.

Since an empty string reads the same forward and backward, it is a palindrome.
 
---

## Constraints:
<pre>
1 <= s.length <= 2 * 10<sup>5</sup>
s consists only of printable ASCII characters.
</pre>