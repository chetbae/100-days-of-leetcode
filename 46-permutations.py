class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # create output array
        ans = []

        # use backtracking to find all permutations
        self.search(nums, [], ans)

        return ans


    def search(self, nums, permutation, ans):
        # if no more integers left, append permutation to output array
        if not nums:
            ans.append(permutation)
            return
        
        # otherwise keep searching each nums
        for i in range(len(nums)):
            # make current permutation with nums[i]
            current = permutation + [nums[i]]
            
            # exclude nums[i] from search to ensure permutation and not combination
            candidates = nums[:i] + nums[i+1:]

            self.search(candidates, current, ans)
