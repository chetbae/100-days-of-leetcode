class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # intuition: find the first non-descending element from the right and set a pointer.
        # then find the next largest element on the right side and swap with first element
        # finally sort the right side in ascending order

        n = len(nums)

        # if single element or empty array, only 1 permutation
        if n <= 1:
            return nums
        
        # find the first element
        left = n - 2

        while left >= 0:
            
            # found
            if nums[left] < nums[left+1]:
                break
            
            left -= 1
            
        # if nums is all descending, return ordered list aka first permutation
        if left == -1:
            nums.reverse()
            return

        # otherwise binary search the rightmost descending list for next largest element
        lo, hi = left+1, n-1
        target = nums[left]

        # always next largest from target
        while lo < hi :
            # right/upper mid
            mid = lo + (hi-lo+1) // 2 

            if nums[mid] > target:
                lo = mid
            else:
                hi = mid - 1
        
        # next largest element
        right = lo

        # swap first element and nextLargest element
        nums[left], nums[right] = nums[right], nums[left]

        # finally sort the rightmost array
        nums[left+1:] = nums[n-1:left:-1]


        
        # [1,2,3] -> [1,3,2]
        # [1,3,2] -> [2,3,1] -> [2,1,3]
        # [2,1,3] -> [2,1,3]
        # [2,3,1] -> [3,2,1] -> [3,1,2]
        # [3,1,2] -> [3,2,1]
        # [3,2,1] -> all decreasing -> [1,2,3]
        
        # [1,2,3,4] -> [1,2,4,3]
        # [1,2,4,3]
        # [1,3,2,4]
        # [1,3,4,2] -> [1,4,3,2] -> [1,4,2,3]
        # [1,4,2,3]
        # [1,4,3,2]
        # [2,1,3,4]

        # [1,2]
        # [2,1]

        # [1,1,5] -> [1,5,1]
        # [1,5,1] -> [5,1,1]
        # [5,1,1] -> 