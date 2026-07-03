class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = None

    def addNum(self, num: int) -> None:
        # find size of heap
        # get smallest value from heap
        if not self.minHeap:
            heapq.heappush(self.minHeap, num)
        elif num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, num * -1)
        if len(self.minHeap) - len(self.maxHeap) == 2: # move minheap to maxheap
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val * -1)
        elif len(self.maxHeap) - len(self.minHeap) == 2:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)

        # the heaps can only differ by 1 in size
        # if differs by more move one to other heap

    def findMedian(self) -> float:
        if len(self.minHeap) - len(self.maxHeap) == 0:
            return (self.minHeap[0] + (self.maxHeap[0] * -1)) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0] * -1
        
        