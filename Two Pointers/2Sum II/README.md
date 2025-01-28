# 2Sum Part 2

> Although it's written in **bold**, I managed to ignore the part about returning the indices as 1-indexed

Start off with a left and right pointer where left is 0 and right is the last element

Set the sum as `numbers[left] + numbers[right]` and use it to compare against `target` to determine how the pointers are going to move. Since there's only 1 solution, we instantly return the indices of the elements that sum to target.

``` python
if sum == target:
    return [left + 1, right + 1]
    elif sum > target:
        right -= 1
    else:
        left += 1
```

