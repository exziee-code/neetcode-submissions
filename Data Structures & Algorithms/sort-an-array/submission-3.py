class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        #where n be the size of an array
        if len(nums) > 1: #O(1)
            #dividing the array nums
            left_arr = nums[:len(nums)//2] #O(n)
            right_arr = nums[len(nums)//2 :] #O(n)

            #recursion
            #O(log n)
            self.sortArray(left_arr)
            self.sortArray(right_arr)
        
            i = 0 #left_arr idx, O(1)
            j = 0 #right_arr idx, O(1)
            k = 0 #main array idx, O(1)

            #O(n)
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
            
            #to append the remaining elements in the left array to nums, O(n)
            while i < len(left_arr):
                nums[k] = left_arr[i]
                k += 1
                i += 1
            
            #to append the remaining elements in the right array to nums, O(n)
            while j < len(right_arr):
                nums[k] = right_arr[j]
                j += 1
                k += 1
        
        return nums
        #total = O(n·log n)
        



















