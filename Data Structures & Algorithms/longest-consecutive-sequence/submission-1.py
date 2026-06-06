class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for i in nums:
            if (i-1) not in num_set:
                length = 1
                while (i+1) in num_set:
                    length += 1
                    i += 1
                if length > result : result = length
        return result