# Products of Array Except Self

> Just as I've abandoned Emacs in advent of code in favor of vsCode because I wasted a lot of time wanting a debugger to work that is not DAP because why emulate vsCode when you can just use it. Back to .md

### Full Code 
```python
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_arr = [0] * n
        suffix_arr = [0] * n
        prefix_multiplier = 1
        suffix_multiplier = 1

        for i in range(n):
            j = -i -1
            prefix_arr[i] = prefix_multiplier
            suffix_arr[j] = suffix_multiplier
            prefix_multiplier *= nums[i]
            suffix_multiplier *= nums[j]

        return [p * s for p, s in zip(prefix_arr, suffix_arr)]
```