class Solution:
    def maxArea(self, height: List[int]) -> int:
        # make left and right pointers starting at widest container
        lo, hi = 0, len(height)-1

        # track largest area
        A, maxLo, maxHi, direction = 0, lo, hi, -1 # 0 for going right, 1 for going left, -1 initially

        # check containers
        while lo < hi:
            
            # check going right direction
            if direction == 0 and height[lo] <= height[maxLo]:
                lo += 1
                continue
            
            # check going left direction
            elif direction == 1 and height[hi] <= height[maxHi]:
                hi -= 1
                continue

            # calculate current area
            area = min(height[lo], height[hi]) * (hi-lo)
            
            # if area is greater than max, update
            if area > A:
                A, maxLo, maxHi = area, lo, hi

            # for any height inbetween, the greater height will contain more or less area than the current area (A-B), while the lesser height can only be less than current area
            
            # move lesser pointer, if same either direction doesn't matter (here left is priority)
            if height[lo] > height[hi]:
                hi -= 1
            else:
                lo += 1
        
        return A