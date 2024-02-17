# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/description/

class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k
        self.head = 0
        self.tail = 0
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.tail % self.size] = value
        self.tail += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head % self.size]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.tail - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return self.tail - self.head == self.size
