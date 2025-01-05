from collections import defaultdict
from typing import Counter, List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            groups[sorted_str].append(s)
        return list(groups.values())
            
Solution().groupAnagrams(strs=["act","pots","tops","cat","stop","hat"])

