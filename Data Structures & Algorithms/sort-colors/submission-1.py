class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0 #indicates 0
        j = len(nums) - 1 #indicates 2
        k = 0 #indicates current

        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
            
            elif nums[k] == 2:
                nums[k], nums[j]  = nums[j], nums[k]
                j -= 1
                k -= 1
            
            k += 1
        