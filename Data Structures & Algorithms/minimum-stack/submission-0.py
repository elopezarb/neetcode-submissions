class MinStack:

    def __init__(self):
        
        self._stack = []
        self._minVals = []
        

    def push(self, val: int) -> None:
        
        self._stack.append(val)
        
        if not self._minVals:
            self._minVals.append(val)
            
        else:
            if val < self._minVals[-1]:
                self._minVals.append(val)
            else:
                self._minVals.append(self._minVals[-1])
                
            
        

    def pop(self) -> None:
        
        if not self._stack:
            raise ValueError("Cannot pop an empty MinStack")
        else:
            self._stack.pop()
            
            self._minVals.pop()
                
        

    def top(self) -> int:
        if not self._stack:
            raise ValueError("Cannot top an empty MinStack")
        else:
            return self._stack[-1]
    

    def getMin(self) -> int:
        
        if not self._stack:
            raise ValueError("Cannot getMin an empty MinStack")
        else:
            return self._minVals[-1]
    

        
