# iterative solution by extending power set for each element
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # create power set, starting with empty set
        powerSet = [[]]

        # add possible subsets to power set, adding one element at a time
        for element in nums:

            # update powerSet by retaining previous subsets and including subsets made by adding current element
            powerSet += [subset + [element] for subset in powerSet]
        
        return powerSet

# one liner
