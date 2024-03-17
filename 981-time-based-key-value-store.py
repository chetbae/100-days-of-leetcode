class TimeMap:

    def __init__(self):
        self.db = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key doesn't yet exist, create empty array
        if key not in self.db:
            self.db[key] = []
        
        # append timestamp-value to timestamp array
        # timestamps are strictly increasing so no need to sort
        self.db[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # if there is no hit on a key, there is no timestamp-values
        if key not in self.db:
            return ""
        
        # make a ref to the timestamp array
        arr = self.db[key]

        # binary search
        lo, hi = 0, len(arr)

        while lo < hi:
            mid = (lo+hi) // 2
            time, val = arr[mid]
            if time == timestamp:
                return val
            elif time < timestamp:
                lo = mid+1
            else:
                hi = mid
        
        return arr[hi-1][1] if hi > 0 else ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)