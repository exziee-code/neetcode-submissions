class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for i in strs:
            temp = str(len(i)) + "#" + i
            enc.append(temp)
        return "".join(enc)

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            word = s[j+1: j+ 1 + length]
            print(word)
            dec.append(word)
            i = j+ 1 + length
        return dec