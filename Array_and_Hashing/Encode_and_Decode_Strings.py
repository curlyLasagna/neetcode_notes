from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        separator = "#"
        for i, s in enumerate(strs):
            strs[i] = f"{len(s)}{separator}{s}"

        return ''.join(strs)

    def decode(self, s: str):
        str_len = ''
        num_len = 0
        res = []
        i = 0
        
        while i < len(s):
            if not s[i].isalnum():
                num_len = int(str_len)
                res.append(s[i + 1: i + 1 + num_len])
                i += num_len + 1
                str_len = ''
                num_len = 0
                continue
            str_len += s[i]
            i += 1
            
        return res
