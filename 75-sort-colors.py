# two-pass solution O(n) time, O(1) space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # count number of 1, 2, 3's
        zero, one, two = 0, 0, 0

        for num in nums:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            else:
                two += 1

        # modify nums for the number of one two and threes
        for i in range(zero):
            nums[i] = 0
        
        for i in range(zero, zero+one):
            nums[i] = 1
        
        for i in range(zero+one, zero+one+two):
            nums[i] = 2

# one-pass solution O(n) time, O(1) space **dutch partitioning method
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # make ptrs for zero, one, and two
        zero = 0
        one = 0
        two = len(nums) - 1 

        # terminate when ptr one is greater than or eq to ptr two
        while one <= two:

            # case A: ptr one == 0
            if nums[one] == 0:
                
                # swap elements at ptr zero and one
                # if ptrs are the same, then it simply increments to check next element
                # if ptr one is ahead of ptr zero, then if ptr one == 0, swapping ensures 0 is at the head of zeroes and 1 is at the head of ones.
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            
            # case B: ptr one == 1
            elif nums[one] == 1:

                # the 1 is at the right place (for now), increment and continue
                one += 1
            
            # case C: ptr one == 2
            else:

                # swap elements at ptr one and two
                nums[one], nums[two] = nums[two], nums[one]

                # now ptr two == 2, so decrement for next (previous) element in array
                two -= 1

                # don't increment one as it is not guaranteed to be 1, continue and check cases in loop
        
        # case A ensures elements ptr zero and below is 0
        # case A and B ensures elements between zero and one is 1 
        # case C ensures elements beyond ptr two is 2
        # termintation conditions are met, meaning ptr one > ptr two so all elements are checked
