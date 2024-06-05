class Solution:
    def trap(self, height: List[int]) -> int:
        # Intuition: work inwards from both ends, sum up water incrementally.

        # Say we have left and right peaks, each the highest in their respective directions, and
        # assume everything leftwards and rightwards has been filled optimally.
        # Then, whatever heights come between them, we now at least heights lesser than both beaks
        # can be filled up to min(left, right). 

        water = 0
        left, right = 0, len(height)-1

        # track highest peaks
        leftPeak = rightPeak = 0
        
        while left < right:

            # if left is shorter than right, water filled from the left can be AT MOST up to left peak
            if height[left] <= height[right]:

                # if current left is peak, no water can be collected -> update peak
                if height[left] >= leftPeak:
                    leftPeak = height[left]
                # otherwise update water sum
                else:
                    water += leftPeak - height[left]
                
                left += 1
            
            # conversely, if left is greater than right, water filled from right can be AT MOST up to right peak
            else: 

                if height[right] >= rightPeak:
                    rightPeak = height[right]
                else:
                    water += rightPeak - height[right]
                
                right -= 1
        
        return water
            
        
