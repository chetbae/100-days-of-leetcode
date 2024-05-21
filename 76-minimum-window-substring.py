class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case: string is shorter than target string
        n = len(s)
        if n < len(t):
            return ""

        # initialize array counter for A-Z/a-z alphabet
        counter = [0] * 58 # A: 65, z: 122
        
        # track count for # of missing letters
        missing = len(t)
        
        # populate counter for letters in target string
        for c in t:
            i = ord(c) - ord('A')
            counter[i] += 1
        
        l, r = 0, 0
        start, minLen = 0, float('inf')
        
        # 1) move right pointer until valid substring, 2) move left pointer until no longer valid substring
        # this ensures smallest window for a valid substring
        while r < n:
            i = ord(s[r]) - ord('A')
            
            # pos integer indicates a match in target string, decrement missing count
            if counter[i] > 0:
                missing -= 1

            # decrement counter for current letter
            counter[i] -= 1

            # move right pointer
            r += 1

            # if all letters from target string are in window
            while missing == 0:

                # if window is smaller than prev, save
                if r - l < minLen:
                    start, minLen = l, r-l
                
                # add letter back to counter
                i = ord(s[l]) - ord('A')
                counter[i] += 1

                # increment missing count if letter goes positive (r ptr decremented, only way for l ptr to go positive is to have been in target string)
                if counter[i] > 0:
                    missing += 1

                # increment left pointer
                l += 1
        
        # if no substring found, return empty string
        return "" if minLen == float('inf') else s[start:start+minLen]

        