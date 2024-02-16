# 225. Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/description/

from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
            
        ans = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        
        return ans

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
            
        ans = self.q1[0]
        self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1
        
        return ans

    def empty(self) -> bool:
        return len(self.q1) == 0
