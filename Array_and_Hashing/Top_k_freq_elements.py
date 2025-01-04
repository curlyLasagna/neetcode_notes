from typing import Counter, List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myHash = Counter(nums)
        myRes = []
        max_freq = 0
        for i in range(k):
            max_freq = max(myHash, key=myHash.get)
            myRes.append(max_freq)
            del myHash[max_freq]
            print(myHash)
        return myRes

print(Solution().topKFrequent([1,1,1,2,2,3], k = 2))
