class MinStack:

    def __init__(self):
        self.stack_list = [] 

    def push(self, val: int) -> None:
        self.stack_list.append(val)
        
    def pop(self) -> None:
        self.stack_list.pop()        

    def top(self) -> int:
        return self.stack_list[-1]

    def getMin(self) -> int:
        return min(self.stack_list)
        
