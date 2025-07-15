# 3136. Valid Word

A word is considered valid if:

<li>
It contains a <b>minimum</b> of 3 characters.
</li>
<li>
It contains only digits (0-9), and English letters (uppercase and lowercase).
</li>
<li>
It includes <b>at least</b> one <b>vowel</b>.
</li>
<li>
It includes <b>at least</b> one <b>consonant</b>.
</li>
</br>
You are given a string word.

Return true if word is valid, otherwise, return false.

## Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.

A consonant is an English letter that is not a vowel.
 

## Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

## Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

## Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.

 

## Constraints:
<li>
1 <= word.length <= 20
</li>
<li>
<b>word</b> consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
</li>