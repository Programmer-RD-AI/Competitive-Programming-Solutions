class MyQueue:
    def __init__(self):
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        return self.data.pop(0)

    def peek(self) -> int:
        return self.data[0]

    def empty(self) -> bool:
        return True if self.data == [] else False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(x=1)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
