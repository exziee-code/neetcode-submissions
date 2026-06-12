class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) > 1:
            #dividing the array nums
            left_arr = nums[:len(nums)//2]
            right_arr = nums[len(nums)//2 :]

            #recursion
            self.sortArray(left_arr)
            self.sortArray(right_arr)
        
            i = 0 #left_arr idx
            j = 0 #right_arr idx
            k = 0 #main array idx

            while i < len(left_arr) and j < len(right_arr):
                #check if left_arr i less then right_arr j
                if left_arr[i] < right_arr[j]:
                    nums[k] = left_arr[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = right_arr[j]
                    j += 1
                    k += 1
            
            #to append the remaining elements in the left array to nums
            while i < len(left_arr):
                nums[k] = left_arr[i]
                k += 1
                i += 1
            
            #to append the remaining elements in the right array to nums
            while j < len(right_arr):
                nums[k] = right_arr[j]
                j += 1
                k += 1
        
        return nums