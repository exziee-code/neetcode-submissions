class Solution:
    def sortColors(self, nums: List[int]) -> None:
        freq = {0 : 0,1 : 0, 2: 0}
        for i in nums:
            freq[i] += 1
        
        idx = 0
        for key, value in freq.items():
            for _ in range(value):
                nums[idx] = key
                idx += 1
