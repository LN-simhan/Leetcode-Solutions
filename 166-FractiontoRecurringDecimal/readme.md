# 166. Fraction to Recurring Decimal

Given two integers representing the <code>numerator</code> and <code>denominator</code> of a fraction, return <i>the fraction in string format.</i>

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return <b>any of them</b>.

It is <b>guaranteed</b> that the length of the answer string is less than <code>10<sup>4</sup></code> for all the given inputs.

---

## Example 1:
<pre>
Input: numerator = 1, denominator = 2
Output: "0.5"
</pre>

## Example 2:
<pre>
Input: numerator = 2, denominator = 1
Output: "2"
</pre>

## Example 3:
<pre>
Input: numerator = 4, denominator = 333
Output: "0.(012)"
</pre>

---

## Constraints:
<pre>
-2<sup>31</sup> <= numerator, denominator <= 2<sup>31</sup> - 1
denominator != 0
</pre>