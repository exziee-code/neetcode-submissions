class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 #O(1)
        right = len(height) - 1 #O(1)
        result = 0 #O(1)
        left_max = height[left] #O(1)
        right_max = height[right] #O(1)
        
        while left < right: #O(n) let n be the total element in the list
            #this code will always keep the max element
            #move the left pointer forward
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            #moves the right pointer backword
            else:
                right -=1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        
        return result
        # total = O(n)