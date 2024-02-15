# 61. Rotate List
# https://leetcode.com/problems/rotate-list/description/

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        n = 0
        
        while curr.next:
            curr = curr.next
            n += 1
        
        if n == 0:
            return head
        
        k %= n
        
        if k == 0:
            return head
        
        front = dummy
        for i in range(n - k):
            front = front.next
        
        back = front
        for j in range(k):
            back = back.next
        front.next, dummy.next = back.next, front.next
        back.next = head
        
        return dummy.next
