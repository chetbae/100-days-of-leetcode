class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        left, right = 0, 0

        for i in range(len(nums)):
            left = (left or 1) * nums[i]
            right = (right or 1) * nums[-1-i]

            ans = max(ans, max(left, right))
        
        return ans