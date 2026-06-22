from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictT = defaultdict(int)
        dictS = defaultdict(int)

        for strs in s:
            dictS[strs] += 1
        
        for strs in t:
            dictT[strs] += 1
        
        return dictS == dictT