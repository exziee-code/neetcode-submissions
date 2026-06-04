class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [] #O(1)
        for i in strs: #O(n)
            new = str(len(i))+"#"+i # k is the legth of each string
            #O(log k) + O(k) = O(k)
            encoded.append(new) #O(1)
        return "".join(encoded) #O(n)
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded = s[j+1:j+1+length]
            result.append(decoded)
            i = j+1+length
        return result