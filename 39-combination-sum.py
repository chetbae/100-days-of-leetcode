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

        