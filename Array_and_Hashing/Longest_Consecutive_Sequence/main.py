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

print(Solution().longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))

