class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        maxCount = 0
        count = [0] * 26
        start = 0

        for end in range(n):
            i = ord(s[end]) - ord('A')
            count[i] += 1
            maxCount = max(maxCount, count[i])

            while end - start + 1 - maxCount > k:
                j = ord(s[start]) - ord('A')
                count[j] -= 1
                start += 1
            
            ans = max(ans, end-start+1)
        
        return ans