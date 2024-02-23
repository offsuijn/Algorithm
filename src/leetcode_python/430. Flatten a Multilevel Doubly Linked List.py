# 430. Flatten a Multilevel Doubly Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        
        while curr:
            if curr.child:
                self.merge(curr)
                
            curr = curr.next
            
        return head

    def merge(self, curr: 'Optional[Node]') -> None:
        child = curr.child
        
        while child.next:
            child = child.next
        
        if curr.next:
            curr.next.prev, child.next = child, curr.next
        
        curr.next, curr.child.prev = curr.child, curr
        curr.child = None
        
