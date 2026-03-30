class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        self.st.append(val)

    def pop(self) -> None:
        if self.st:
            self.st.pop()

    def top(self) -> int:
        if self.st:
            return self.st[-1]

    def getMin(self) -> int:
        temp = []
        mini = self.st[-1]
        while len(self.st):
            mini = min(mini, self.st[-1])
            temp.append(self.st[-1])
            self.st.pop()

        while len(temp):
            self.st.append(temp.pop())

        return mini

