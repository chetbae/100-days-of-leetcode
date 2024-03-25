class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        # keep track of max_palindrome
        max_palindrome = ""

        # track which index to search next
        idx = 0

        # consider each character as a start point
        while idx < len(s):
            
            # make pointers
            left = right = idx

            # set right pointer end of same chars
            while right+1 < len(s) and s[right+1] == s[left]:
                right += 1
            
            # set idx to char next to s[right], no need to search same char array
            idx = right + 1

            # expand on both sides until out of bounds or not palindrome
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            
            # if current palindrome is longer than previous, update
            if right-left+1 > len(max_palindrome):
                max_palindrome = s[left:right+1]
        
        return max_palindrome
        



