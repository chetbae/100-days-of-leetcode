class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # at least O(k x n) - search through all n elements in k lists
        # make a min heap of one element from each list
        # intuition: pop the min element, replace with next element from same list so one number from each k lists condition is satisfied
        # as lists are in non-decreasing order, the replacement of an element from kth lists will be the next smallest range possible
        # maintain a max heap as well for max range, no need for replacement as only greater elements will be pushed
        
        minheap = []
        maxheap = []
        
        for i, arr in enumerate(nums):        
            if arr:
                num = arr.pop(0)
                heapq.heappush(minheap, (num, i))
                heapq.heappush(maxheap, -num)
        
        minRange = [minheap[0][0], -maxheap[0]]

        # go through k lists, update minRange
        # stop condition is when min element is last element of kth list -> non decreasing condition means keeping min element and any replacing elements from other lists will only get equal or larger range
        while True:
            # x is smallest element, k is its list index
            x, k = heapq.heappop(minheap)

            # termination condition:
            if not nums[k]:
                break
            
            # replacement
            replacement = nums[k].pop(0)

            heapq.heappush(minheap, (replacement, k))
            heapq.heappush(maxheap, -replacement)

            # update minRange if needed
            c, d = minRange
            a, b = minheap[0][0], -maxheap[0]

            # no need to compare equal ranges since we're working our way upwards, so other equal ranges will have larger magnitudes because of their starting number
            if b - a < d - c:
                minRange = [a, b]
        
        return minRange

