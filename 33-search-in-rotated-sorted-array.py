class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # look for pivot
        left, right = 0, len(nums) - 1

        # set pivot to 0, i.e. not rotated
        pivot = 0

        # if nums is rotated, find pivot: time complexity O(logn)
        if nums[right] < nums[left]:
            # binary search
            while left < right:

                # find midpoint
                mid = (left + right) // 2

                # if mid is more than right, pivot is in right bisection
                # moves right first to converge on smallest element (pivot), not the largest element
                if nums[mid] > nums[right]:
                    left = mid + 1

                #  otherwise pivot is in left bisection
                else:
                    right = mid
            
            # after convergence, set pivot
            pivot = left
        
        # binary search with adjusting for pivot for element: time complexity O(logn)
        
        # length of nums
        n = len(nums)

        # set left and right adjusting for pivot, if no pivot, pivot = 0
        left, right = pivot, pivot + len(nums) - 1

        while left <= right:
            mid = floor((right + left) / 2)

            # to account for pivot, the mid value is mid mod len(nums)
            val = nums[mid % n]

            # if mid is greater than target, look in left bisection
            if val > target:
                right = mid - 1

            # if mid is lesser than target, look in right bisection
            elif val < target:
                left = mid + 1

            # if mid is target, return position accounting for pivot
            elif val == target:
                return mid % n
        
        # if exited binary search without returning, no target
        return -1