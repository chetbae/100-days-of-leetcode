class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # if all array were unique, there would be n + 1 unique elements with a max value of n
        # but since 1 <= nums[i] <= n, there are only n-1 unique elements available -> contradiction
        # therefore there must be at least one duplicate

        # if we view the array as a list of pointers, where nums[i] points to index of the next element, then there will be 2 'nodes' that point to the same target, therefore creating a loop

        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # now that fast = slow = meeting point in the cycle, find entry point
        # move one pointer from the start and one from the meeting point, they meet at entry point aka duplicate (1)
        
        a, b = 0, fast

        while a != b:
            a = nums[a]
            b = nums[b]

        return a

# (1) proof by leetcode user changjinglu
# When they meet, assume slow tag move s steps, fast tag move 2s steps, the circle length is c.
# There must be:

# 2s = s + n*c

# => s = n*c....(1)

# Then, assume the length from start point to entry point is x, and the length from the entry
# point to the meet point is a.
# There must be: s = x+a....(2)

# So, from (1) and (2)

# x+a = s = n*c

# => x+a = n*c

# => x+a = (n-1)*c+c

# => x = (n-1)*c+c-a

# c-a means the length from the meetpoint to the entry point.

# LHS means: the new tag from start point move x steps.

# RHS means: the slow tag moves (n-1) cycles plus the length from the meetpoint to the entry point.

# So, we can get the entry point when the new tag meet the slow tag.