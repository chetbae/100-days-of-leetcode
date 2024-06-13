class MedianFinder:

    def __init__(self):
        self.top = []
        self.bottom = []

    def addNum(self, num: int) -> None:
        self.pushheap(self.top, num)
        self.pushheap(self.bottom, -self.popheap(self.top))

        if len(self.top) < len(self.bottom):
            self.pushheap(self.top, -self.popheap(self.bottom))

    def findMedian(self) -> float:
        n, m = len(self.top), len(self.bottom)

        if n == m:
            return (self.top[0] - self.bottom[0]) / 2
        else:
            return self.top[0]
    
    def pushheap(self, heap, num) -> None:
        heap.append(num)
        i = len(heap) - 1
        parent = (i-1) // 2

        while parent >= 0 and heap[parent] > heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            
            i = parent
            parent = (i-1) // 2

    def popheap(self, heap) -> int:
        if len(heap) <= 1:
            return None if not heap else heap.pop(0)

        out = heap[0]
        heap[0] = heap.pop(-1)
        
        parent = 0
        lchild, rchild = 1, 2
        n = len(heap)

        while lchild < n:
            
            # case: single child
            if lchild == n-1:
                if heap[parent] > heap[lchild]:
                    heap[parent], heap[lchild] = heap[lchild], heap[parent]
                break
            
            smallChild = lchild if heap[lchild] < heap[rchild] else rchild

            # if parent <= smallest child, conditions for heap are met
            if heap[parent] <= heap[smallChild]:
                break
            
            # otherwise swap with smallest child
            heap[parent], heap[smallChild] = heap[smallChild], heap[parent]

            parent = smallChild
            lchild, rchild = 2*parent+1, 2*parent+2
        
        return out
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()