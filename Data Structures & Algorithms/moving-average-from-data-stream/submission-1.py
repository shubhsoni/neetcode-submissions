class MovingAverage:

    def __init__(self, size: int):
        from collections import deque
        self.size = size
        self.seen = deque()
        self.last = 0
        self.sum = 0
        

    def next(self, val: int) -> float:
        self.seen.append(val)
        if len(self.seen)>self.size:
            self.last = self.seen.popleft()

        self.sum = self.sum - self.last + val
        ma = self.sum/min(self.size,len(self.seen))
        return ma

        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
