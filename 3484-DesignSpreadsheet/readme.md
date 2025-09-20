# 3484. Design Spreadsheet

A spreadsheet is a grid with 26 columns (labeled from <code>'A'</code> to <code>'Z'</code>) and a given number of <code>rows</code>. Each cell in the spreadsheet can hold an integer value between 0 and 105.

Implement the <code>Spreadsheet</code> class:
<ul>
<li><code>Spreadsheet(int rows)</code> Initializes a spreadsheet with 26 columns (labeled <code>'A'</code> to <code>'Z'</code>) and the specified number of rows. All cells are initially set to 0.
<li><code>void setCell(String cell, int value)</code> Sets the value of the specified <code>cell</code>. The cell reference is provided in the format <code>"AX"</code> (e.g., <code>"A1"</code>, <code>"B10"</code>), where the letter represents the column (from <code>'A'</code> to <code>'Z'</code>) and the number represents a <b>1-indexed</b> row.
<li><code>void resetCell(String cell)</code> Resets the specified cell to 0.
<li><code>int getValue(String formula)</code> Evaluates a formula of the form <code>"=X+Y"</code>, where <code>X</code> and <code>Y</code> are either cell references or non-negative integers, and returns the computed sum.
</ul>

Note: If <code>getValue</code> references a cell that has not been explicitly set using <code>setCell</code>, its value is considered 0.

---

## Example 1:
<pre>
<b>Input:</b>
["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]
</pre>
<pre>
<b>Output:</b>
[null, 12, null, 16, null, 25, null, 15]
</pre>
<pre>
<b>Explanation</b>

Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns
spreadsheet.getValue("=5+7"); // returns 12 (5+7)
spreadsheet.setCell("A1", 10); // sets A1 to 10
spreadsheet.getValue("=A1+6"); // returns 16 (10+6)
spreadsheet.setCell("B2", 15); // sets B2 to 15
spreadsheet.getValue("=A1+B2"); // returns 25 (10+15)
spreadsheet.resetCell("A1"); // resets A1 to 0
spreadsheet.getValue("=A1+B2"); // returns 15 (0+15)
</pre>

---

## Constraints:
<pre>
<ul>
<li>1 <= rows <= 10<sup>3</sup>
<li>0 <= value <= 10<sup>5</sup>
<li>The formula is always in the format "=X+Y", where X and Y are either valid cell references or non-negative integers with values less than or equal to 10<sup>5</sup>.
<li>Each cell reference consists of a capital letter from 'A' to 'Z' followed by a row number between 1 and rows.
<li>At most 10<sup>4</sup> calls will be made in total to setCell, resetCell, and getValue.
</ul>
</pre>