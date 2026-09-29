class Deque:
    
    def __init__(self):
        self.queue = []


    def isEmpty(self) -> bool:
        return not self.queue
        

    def append(self, value: int) -> None:
        self.queue.append(value)
        

    def appendleft(self, value: int) -> None:
        self.queue = [value] + self.queue
        

    def pop(self) -> int:
        if not self.isEmpty():
            pop =  self.queue[-1]
            self.queue = self.queue[:-1]
            return pop
        else:
            return -1
        

    def popleft(self) -> int:
        
        if not self.isEmpty():
            pop = self.queue[0]
            self.queue = self.queue[1:]
            return pop
        else:
            return -1
        
