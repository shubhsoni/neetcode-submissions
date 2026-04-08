class MovingAverage:

    def __init__(self, size: int):
        from collections import deque
        self.size = size
        self.seen = []
        

    def next(self, val: int) -> float:
        self.seen.append(val)
        ma = sum(self.seen[-self.size:])/len(self.seen[-self.size:])
        return ma

        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
