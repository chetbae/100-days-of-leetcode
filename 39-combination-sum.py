# BACKTRACKING SOLUTION
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # create out array
        ans = []

        # use backtracking to find all possible unique combinations that add to target sum
        self.search(candidates, target, [], ans)

        # return answer
        return ans
    
    def search(self, nums, diff, path, ans):
        # if diff < 0, then sum of path > target, discard
        if diff < 0:
            return
        
        # if diff == 0, then path sums to target and is a solution
        if diff == 0:
            ans.append(path)
            return
        
        # otherwise sum of path is still less than target, and we run search again with all candidates
        for i in range(len(nums)):

            # note: to find unique combinations only, for each search we limit the candidates from i to n, not 0 to n
            self.search(nums[i:], diff-nums[i], path+[nums[i]], ans)

# DP SOLUTION
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # create dp array for values of 1 to target, inclusive
        # for each i, dp[i] = array of combinations that add up to i
        dp = [[] for _ in range(target+1)]
        
        # run for each candidate
        for c in candidates:

            # for each candidate, find combinations for each value from c to target
            # candidates larger than target are ignored
            for i in range(c, target+1):  

                # add each candidate as a combination for dp[candidate]
                if i==c:
                    dp[c].append([c])

                # for each existing combo of sum i-c, adding c is a new combination for i
                for combo in dp[i-c]:

                    # add new combination for dp[i]
                    dp[i].append(combo + [c])
        
        # after running dp, all possible combinations are stored in dp[target]
        return dp[target]