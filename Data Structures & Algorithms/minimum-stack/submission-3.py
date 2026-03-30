class MinStack:

    def __init__(self):
        self.st = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.st.append(val)
        top = self.minStack[-1] if self.minStack else val
        mini = min(val, top)
        self.minStack.append(mini)

    def pop(self) -> None:
        self.st.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
