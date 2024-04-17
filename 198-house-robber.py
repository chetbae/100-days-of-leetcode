class Solution:
    def rob(self, nums: List[int]) -> int:
        # for nums up to i, dp[i-2] + house_i OR dp[i-1]
        dp = [0] * (len(nums)+1)

        # for 0 to 0 elements, max rob is 0. for 0 to 1 elements, max rob is 1 (if nums is positive)
        dp[1] = nums[0]

        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
        
        return dp[-1]

# space optimized
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, nums[0] # dp[0] -> dp[i-2], dp[1] -> dp[i-1]

        # index 0, 1 are prev1, prev2. calculate the rest of the dynamic prog array
        for i in range(2, len(nums)+1):
            prev1, prev2 = prev2, max(prev1 + nums[i-1], prev2)
        
        return prev2
