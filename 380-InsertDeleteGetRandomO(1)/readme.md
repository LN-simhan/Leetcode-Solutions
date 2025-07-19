# 380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.

<b>bool insert(int val)</b> : Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.

<b>bool remove(int val)</b> : Removes an item val from the set if present. Returns true if the item was present, false otherwise.

<b>int getRandom()</b> : Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

---

## Example 1:
<pre>
<b>Input</b>
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
<b>Output</b>
[null, true, false, true, 2, true, false, 2]
</pre>

<b>Explanation</b>
<pre>
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
</pre>

---
## Constraints:
<pre>
-2<sup>31</sup> <= val <= 2<sup>31</sup> - 1
At most 2 * 10<sup>5</sup> calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
</pre>