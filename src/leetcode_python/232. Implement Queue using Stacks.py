# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.top = None

    def push(self, x: int) -> None:
        if not self.stack1:
            if not self.stack2:
                self.top = x
            else:
                while self.stack2:
                    self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) > 1:
            self.top = self.stack2[-2]
        return self.stack2.pop()

    def peek(self) -> int:
        return self.top

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
