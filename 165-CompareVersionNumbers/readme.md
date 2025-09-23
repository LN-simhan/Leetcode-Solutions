# 165. Compare Version Numbers

Given two version strings, <code>version1</code> and <code>version2</code>, compare them. A version string consists of revisions separated by dots <code>'.'</code>. The <b>value of the revision</b> is its <b>integer conversion</b> ignoring leading zeros.

To compare version strings, compare their revision values in <b>left-to-right order</b>. If one of the version strings has fewer revisions, treat the missing revision values as <code>0</code>.

Return the following:
<ul>
<li>If <code>version1 < version2</code>, return -1.
<li>If <code>version1 > version2</code>, return 1.
<li>Otherwise, return 0.
</ul>

---

## Example 1:

Input: version1 = "1.2", version2 = "1.10"
<pre>
Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.
</pre>

## Example 2:
<pre>
Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
</pre>

## Example 3:
<pre>
Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".
</pre>
 
---

## Constraints:
<pre>
1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.
</pre>