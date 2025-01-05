from typing import Counter, List
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
                    return nums
        myHash = Counter(nums)
        return hq.nlargest(k, myHash.keys(), key = myHash.get)
        
print(Solution().topKFrequent([1,1,1,2,2,3], k = 2))
