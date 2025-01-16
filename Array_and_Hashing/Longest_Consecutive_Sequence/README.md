# Longest Consecutive Subsequence

READ THE PROBLEM BEFORE YOU START THINKING!

When I looked at the example, `[0,3,2,5,4,6,1,1]` has an expected output of 7. I was puzzled for a long time until I realized that it doesn't have to be contiguous or consecutive in the original array.

## Intuition

### Sorting

You can sort input array, but that will yield a run time of $O(n\log{n})$, which is slower than the required linear runtime.

### Set

Pass the input array into a set. A set removes duplicates and makes searching much faster since it internally uses hashing.

Loop throughout the set for values that do not have a value less than one because those values are the start of a consecutive sequence.

We keep track of the current length and the max length as we're traversing each sequence.

```python
max_length = 0
myHashSet = set(nums)
for num in myHashSet:
    if num - 1 not in nums:
        start = num
        curr_length = 1
```

This is where the lookup speed of the set comes into play.
Increment `curr_length` until an incremented value from `start` is no longer in the set.
```python
while start + 1 in myHashSet:
    start += 1
    curr_length += 1
```

Compare `current_length` with the `max_length` to get the longest consecutive subsequence

```python
max_length = max(max_length, curr_length)
```

#### Full code

```python
from typing import List
from collections import Counter


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = 0
        max_length = 0
        myHashSet = set(nums)
        for num in myHashSet:
            if num - 1 not in nums:
                start = num
                curr_length = 1
                while start + 1 in myHashSet:
                    start += 1
                    curr_length += 1
                max_length = max(max_length, curr_length)

        return max_length
```