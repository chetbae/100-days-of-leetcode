class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sub = []

        for i, x in enumerate(nums):
            # while elements remain in stack AND x is lesser than last element AND there remain enough nums to make k subsequence
            while sub and x < sub[-1] and n-i >= k - len(sub) + 1:
                sub.pop()
            
            # x is next smallest element for sub, add x if sub is not max capacity
            if len(sub) < k:
                sub.append(x)
        
        return sub