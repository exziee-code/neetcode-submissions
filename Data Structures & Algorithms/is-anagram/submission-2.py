from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = defaultdict(int) #assign a default value of 0 if not exists alreay
        dictT = defaultdict(int) #O(1)
        for i in s: #O(n)
            dictS[i] += 1
        
        for i in t: #O(n)
            dictT[i] += 1
        
        return (dictT == dictS) #O(1)
        #total = O(n)