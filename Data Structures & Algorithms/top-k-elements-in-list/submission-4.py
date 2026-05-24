from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)] # O(n)
        freq = defaultdict(int) #O(1)
        for i in nums: #O(n)
            freq[i] += 1 #O(1), for this loop O(n)
        for key,value in freq.items(): #O(k)
            buckets[value].append(key) #O(1), for this loop O(k)
        result = [] #O(1)
        for i in range(len(buckets)-1,-1,-1): #O(n)
            if buckets[i]: #O(1)
                for j in buckets[i]: #O(u)
                    result.append(j) #O(1)
                    if len(result) == k: #O(1)
                        return result #O(1), total = O(n)+O(k)+(O(n)+O(u)) = O(u)