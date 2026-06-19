class MinStack:

    def __init__(self):
        self.arr = [0]
        self.cur = 0

    def push(self, val: int) -> None:
        if self.cur >= len(self.arr):
            copy = 2 * len(self.arr) * [0]
            for i in range(len(self.arr)):
                copy[i] = self.arr[i]
            self.arr = copy
        self.arr[self.cur] = val
        self.cur += 1

    def pop(self) -> None:
        self.cur -= 1
        return self.arr[self.cur]

    def top(self) -> int:
        return self.arr[self.cur - 1]

    def getMin(self) -> int:
        m = self.arr[0]
        for i in range(self.cur):
            m = min(m, self.arr[i]) 
        return m
        
