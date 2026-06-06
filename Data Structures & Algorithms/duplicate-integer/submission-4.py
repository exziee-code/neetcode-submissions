class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {} #O(1)
        for i in nums:#O(n)
            if i not in dup:#O(1)
                dup[i]=1
            else:
                return True
        return False #total it is O(n)