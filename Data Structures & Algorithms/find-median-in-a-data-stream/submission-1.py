class MedianFinder:

    def __init__(self):
        self.minH = []
        self.maxH = []
        

    def addNum(self, num: int) -> None:
        if not self.minH or num >=  self.minH[0]:
            heapq.heappush(self.minH, num)
        else:
            heapq.heappush(self.maxH, -num)
        if len(self.minH) > len(self.maxH)+1:
            heapq.heappush(self.maxH, - heapq.heappop(self.minH))
        elif len(self.maxH) > len(self.minH)+1:
            heapq.heappush(self.minH, - heapq.heappop(self.maxH))

    def findMedian(self) -> float:
        # print(self.minH)
        # print(self.maxH)
        # print()
        if len(self.minH) == len(self.maxH):
            return (self.minH[0] + (-(self.maxH[0])))/2
        return self.minH[0] if len(self.minH) > len(self.maxH) else -self.maxH[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()