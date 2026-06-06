from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = defaultdict(int)
        for i in nums:
            num[i] +=1
        
        result = 0
        for i in nums:
            temp = []
            start = i
            nxt = i+1
            temp.append(start)
            while nxt in num.keys():
                temp.append(nxt)
                nxt += 1
            result = max(len(temp),result)
        
        return result