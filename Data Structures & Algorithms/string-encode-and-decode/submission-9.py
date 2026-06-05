class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [] #O(1)
        for i in strs: #O(n)
            new = str(len(i))+"#"+i #O(k)
            encoded.append(new) #O(1)
        # total = O(n·k)
        return "".join(encoded) #O(m) let m be the total length of the string
        #total of encode = O(m)

    def decode(self, s: str) -> List[str]:
        result = [] #O(1)
        i = 0 #(1)
        while i < len(s): #O(m) where p is the total number of steps in all iteration
            j = i #O(1)
            while s[j] != '#': #O(d) where d is the number of digits
                j += 1 #O(1)
            length = int(s[i:j]) #O(d) where d be the number of digits
            decoded = s[j+1:j+1+length] #O(k) let k be the length of the word
            result.append(decoded) #O(1)
            i = j+1+length #O(1) because its just addition operation
        return result #O(1)
        #total = O(m)