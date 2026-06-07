class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 #O(1)
        right = len(s) - 1 #O(1)

        while left < right: #O(n) where n be the length of the sting

            # Moves 'left' forward; max total steps across whole program <= N
            while left < right and not s[left].isalnum(): 
                left += 1

            # Moves 'right' backward; max total steps across whole program <= N
            while right > left and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower(): #O(1)
                return False
            
            left += 1
            right -= 1
        
        return True # total = O(n)