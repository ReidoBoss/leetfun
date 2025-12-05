# Design a stack class that supports the push, pop, top, and getMin operations.


# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1)
# O(1) time.


class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []

    def push(self, val: int) -> None:

        if len(self.stack) == 0:
            self.minimumStack.append(val)
        else:
            minimum = min(val, self.minimumStack[-1])
            self.minimumStack.append(minimum)

        self.stack.append(val)

    def pop(self) -> None:
        self.minimumStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # 2
minStack.pop()
print(minStack.getMin())  # 3
