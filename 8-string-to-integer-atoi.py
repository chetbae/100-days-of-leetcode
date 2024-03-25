class Solution:
    def myAtoi(self, s: str) -> int:
        # set sign to 1, set to -1 later if negative
        sign = 1

        # pointers for left and right of valid integer
        left, right = 0, 0

        # ignore whitespace
        while left < len(s) and s[left] == " ":
            left += 1
        
        # if end of string, return 0
        if left == len(s):
            return 0
        
        # adjust signs as needed
        if s[left] == "+":
            left += 1
        elif s[left] == "-":
            left += 1
            sign = -1
        
        # set right to left
        right = left

        # go until non digit
        while right < len(s) and s[right] in "0123456789":
            right += 1
        
        # if no digits, return 0
        if left == right:
            return 0
            
        # parse int
        ans = sign * int(s[left:right])

        # clamp ans to range [-2^31, 2^31 - 1]
        if ans < -2**31:
            return -2**31
        elif ans > 2**31-1:
            return 2**31-1
        
        return ans
        




        

        


