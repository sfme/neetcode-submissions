class MinStack:

    def __init__(self):
        self.stack_list = [] 
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.stack_list:
            self.min_stack.append(min(self.min_stack[-1], val))
        else:
            self.min_stack.append(val)

        self.stack_list.append(val)
        
    def pop(self) -> None:
        self.stack_list.pop()
        self.min_stack.pop()     

    def top(self) -> int:
        return self.stack_list[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
