class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for i in range(1, len(strs)):
            if strs[i] == "" or result == "":
                return ""
            else:
                temp = []
                for j in range(min(len(strs[i]), len(result))):
                    if result[j] == strs[i][j]:
                        print(result[j])
                        temp.append(result[j])
                    else:
                        break
                result = "".join(temp)
    
        return result