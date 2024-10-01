class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self, val):
        self.inStack.append(val)

    def pop(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
                
        return self.outStack.pop()

    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
                
        return self.outStack[-1]

    def empty(self):
        return len(self.inStack) == 0 and len(self.outStack) == 0