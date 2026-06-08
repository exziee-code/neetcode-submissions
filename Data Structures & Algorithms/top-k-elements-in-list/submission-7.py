from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
        
        for key, value in freq.items():
            buckets[value].append(key)
        
        result = []
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]:
                for i in buckets[i]:
                    result.append(i)
                    if len(result) == k:
                        return result