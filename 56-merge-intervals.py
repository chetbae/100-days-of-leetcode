class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals in ascending order
        intervals.sort(key=lambda x: x[0])

        # create output array
        ans = []

        # create variables to track start and stop integers to merge
        start, stop = intervals[0]

        # iterate through all intervals
        for i in range(1,len(intervals)):

            # get start/stop times for current interval
            curStart, curStop = intervals[i]
            
            # if new interval intersects old intervals, merge and update stop
            if curStart <= stop and curStop > stop:
                stop = curStop
            
            # if new interval is wholely within start/stop, merge by doing nothing as stop is bigger than curStop
            elif curStart <= stop and curStop <= stop:
                continue
            
            
            # otherwise they're seperate intervals, append to out array
            else:
                ans.append([start, stop])
                
                # update start/stop for next comparison
                start, stop = curStart, curStop

        # append last interval
        ans.append([start,stop])

        return ans