class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        result = 0
        for i in range(len(nums)):

            if i > 0 and nums[i]-1 in num_set:
                continue
            
            else:
                length = 1
                while length + nums[i] in num_set:
                    length += 1
                if length > result : result = length

        return result