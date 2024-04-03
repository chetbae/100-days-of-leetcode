from collections import Counter 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        # use 2 alphabet arrays and sliding windows to find anagram indices
        ans = []

        # create arrays of size 26 for storing occurences of a-z: ord(char) - ord('a') == index
        sMap, pMap = [0] * 26, [0] * 26
        
        # populates maps for length of the anagram
        for i in range(len(p)):
            sMap[ord(s[i]) - 97] += 1
            pMap[ord(p[i]) - 97] += 1
        
        left, right = 0, len(p) # left inclusive, right exclusive

        while right < len(s):
            
            # check if anagram has been found
            if sMap == pMap:
                ans.append(left)
            
            # add new sliding window char
            sMap[ord(s[right]) - 97] += 1
            sMap[ord(s[left]) - 97] -= 1

            left += 1
            right += 1
        
        # check if anagram has been found
        if sMap == pMap:
            ans.append(left)
        

        return ans