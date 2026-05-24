class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index,value in enumerate(nums):
            dic[value] = index
        for i in range(len(nums)):
            Required = target - nums[i]
            if Required in dic and dic[Required] != i:
                return [i,dic[Required]]
            