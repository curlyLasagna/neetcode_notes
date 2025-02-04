#!/usr/bin/env python3

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        for i in range(len(s2) - len(s1) + 1):
            if Counter(s1) == Counter(s2[i : i + len(s1)]):
                return True

        return False


Solution().checkInclusion(s1="adc", s2="dcda")
