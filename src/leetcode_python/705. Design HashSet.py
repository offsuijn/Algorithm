# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/description/

class MyHashSet:

    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        # if key in self.hashset:
        #     self.hashset.remove(key)
        self.hashset.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset
