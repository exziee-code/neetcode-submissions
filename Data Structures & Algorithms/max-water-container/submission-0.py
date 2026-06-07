class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        result = 0
        while i < len(heights): 
            j = i + 1
            width = 0
            while j < len(heights):
                width += 1
                height = min(heights[i], heights[j])
                result = max(result, (width * height))
                
                j += 1
            i += 1
        return result