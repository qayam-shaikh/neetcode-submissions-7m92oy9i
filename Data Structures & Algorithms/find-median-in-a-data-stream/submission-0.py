class MedianFinder:

    def __init__(self):
        self.heap1=[]
        self.heap2=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap1,-num)
        if self.heap1 and self.heap2 and -self.heap1[0]>self.heap2[0]:
            val=-heapq.heappop(self.heap1)
            heapq.heappush(self.heap2,val)
        
        if len(self.heap1)>len(self.heap2)+1:
            val=-heapq.heappop(self.heap1)
            heapq.heappush(self.heap2,val)

        if len(self.heap2)>len(self.heap1)+1:
            val=heapq.heappop(self.heap2)
            heapq.heappush(self.heap1,-val)


    def findMedian(self) -> float:
        if len(self.heap1)>len(self.heap2):
            return -self.heap1[0]
        elif len(self.heap2)>len(self.heap1):
            return self.heap2[0]
        else:
            return (-self.heap1[0] + self.heap2[0])/2.0







        