from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = defaultdict(int) #assign a default value of 0 if not exists alreay
        dictT = defaultdict(int)
        for i in s:
            dictS[i] += 1
        
        for i in t:
            dictT[i] += 1
        
        return (dictT == dictS)