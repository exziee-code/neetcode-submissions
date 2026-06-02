class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            new = str(len(i))+"#"+i
            encoded += new
        return encoded
        
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