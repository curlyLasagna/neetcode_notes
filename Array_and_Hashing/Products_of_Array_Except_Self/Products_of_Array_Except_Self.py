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

Solution().productExceptSelf([1, 2, 4, 6])
