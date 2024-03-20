# full matrix dp solution: O(n*S) time, O(n*S) space
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum of set1 + set2 is sum of nums, and sum of set1 == set2, so 2 * sum of set 1 or 2 == nums.
        # so finding a set of sum(nums)/2 means there is a partition of equal subset sums
        S = sum(nums)

        # if total sum is odd, a solution set1 == set2 cannot be found
        if S % 2 == 1:
            return False
        
        # modify 01 knapsack to find boolean condition instead of maximizing value
        # subproblem: out of the first ith nums, is there a subset sum of value v
        # dp[i][v] = True | False
        # condition 1: if dp[i-1][v] is True ~ for nums up to i-1th there is already a subset sum of v
        # condition 2: if dp[i-1][v-v_i] is True (v_i is nums[i-1])~ if nums up to i-1th is True for target value minus item ith's value, then dp[i][v] is true as adding item i will make up value v

        # create dp array
        dp = [[False] * (int(S/2)+1) for _ in range(len(nums) + 1)]

        # base case: for none of the nums, a value of 0 is True
        dp[0][0] = True

        # for each num in nums, where i is at nums[i-1] due to indexing
        for i in range(1, len(nums) + 1):
            
            # for each value up to target value sum S/2
            for v in range(int(S/2) + 1):

                # for condition 2, if current num is greater than current value, only condition 1 is valid
                # dp[i-1][v-v_i] out of bounds ~ if v - nums[i-1] < 0

                dp[i][v] = dp[i-1][v] if v - nums[i-1] < 0 else dp[i-1][v] or dp[i-1][v-nums[i-1]]
        
        # for all items, for value S/2, if True there must be a subset sum equal to S/2 and therefore a partition that makes equal subsets
        return dp[len(nums)][int(S/2)]


# one row dp solution: O(n*S) time, O(S) space
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        
        target = totalSum // 2

        # using one row dp
        dp = [False] * (target + 1)
        dp[0] = True

        # run for all items except last
        for i in range(len(nums)-1):

            # update each weight/sum in row from rightmost
            for w in range(target, -1, -1):
                
                # current weight can be made if 1) current weight - nums[i] is True, i.e. current weight can be made by a subset sum by selecting nums[i]
                # or 2) a subset is already summed to current weight by not selecting nums[i]
                dp[w] = dp[w - nums[i]] or dp[w] if w - nums[i] >= 0 else dp[w]
        
        # find if target weight/sum can be found from previous dp row
        return dp[target-nums[-1]] or dp[target] if target - nums[-1] >= 0 else dp[target]
        
# bitwise dp solution O(n) time, O(1) space
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        # if sum is odd, 2 equal subsets can't be found
        if totalSum % 2:
            return False
        
        # knapsack solution - where each iteration including ith item, each bit correlates to if a subset of weight w can be found (where w is the bits position from left to right)
        target = totalSum // 2

        # set leftmost bit to true, as a subset sum of 0 can be made with no items
        row = 1 << target

        # build up the 'rows' (bits) for each num weight
        for w in nums:
            # where each bit is true if previous row bit is true, or if the previous row bit w positions to the left is true, i.e. if selecting current num or not selecting can make weight for bit position
            row |= row >> w

        # a partition can be found if the rightmost bit is 1, i.e. for all items a target value of totalsum/2 can be found
        return row & 1