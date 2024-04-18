class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if net fuel is less than 0, no cycle can be completed
        if sum(gas) - sum(cost) < 0:
            return -1

        # fuel on current trip
        trip = 0

        # best start
        start = 0

        # check each point for solution
        for i in range(len(gas)):
            trip += gas[i] - cost[i]

            # if trip is at deficit, all stations from start to i are sub-optimal
            if trip < 0:
                trip = 0

                # set start to next starting station
                start = i + 1
                
        # check if a full cycle has been run, return index if unique solution exists
        return start