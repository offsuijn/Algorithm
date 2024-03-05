# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random

class RandomizedSet:

    def __init__(self):
        self.hashmap = set()

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        else:
            self.hashmap.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        else:
            self.hashmap.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.hashmap))
