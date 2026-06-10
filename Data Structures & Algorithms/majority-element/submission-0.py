from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        for key, value in freq.items():
            buckets[value].append(key)
        
        for i in range(len(buckets)-1,-1,-1):
            for j in buckets[i]:
                return j