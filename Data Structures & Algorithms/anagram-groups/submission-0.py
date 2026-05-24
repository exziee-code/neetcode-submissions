from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortdict = defaultdict(list) #O(1)
        for i in strs: #O(n)
            sortedstr = "".join(sorted(i)) #O(k) + O(k log k) = O(k log k)
            sortdict[sortedstr].append(i) # O(1), inner loop = O(n . k log k)
        
        lst = [value for key,value in sortdict.items()] #O(n)
        return lst #Total = O(1) + (O(k) + O(n. k log k)) + O(n) = O(n.k log k)