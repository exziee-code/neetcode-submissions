from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        result = []

        for key, value in freq.items():
            buckets[value].append(key)
        
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                for j in buckets[i]:
                    result.append(j)
                    if len(result) == k:
                        return result
