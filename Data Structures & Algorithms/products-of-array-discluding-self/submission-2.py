class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #O(n)
        prefix = 1 #O(1)
        for i in range(len(nums)): #O(n) let n be the total number of elment in nums
            res[i] = prefix #O(1) because its just assignment
            prefix *= nums[i] #O(1) because its just multiplication and assignment
        
        sufix = 1 #O(1)
        for i in range(len(nums)-1,-1,-1): #O(n)
            res[i] *= sufix #O(1)
            sufix *= nums[i] #O(1)
        
        return res #O(1)