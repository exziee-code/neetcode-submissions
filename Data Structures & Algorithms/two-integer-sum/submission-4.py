class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for index, value in enumerate(nums):
            freq[value] = index
        
        for i in range(len(nums)):
            need = target - nums[i]
            if need in freq and freq[need] != i:
                return [i, freq[need]]