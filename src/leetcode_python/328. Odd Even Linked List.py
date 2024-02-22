# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/description/

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        slow, prev = head, head
        curr = head.next
        cnt = 0
        
        while curr:
            if (cnt % 2) == 1:
                prev.next = curr.next
                slow.next, curr.next = curr, slow.next
                
                slow = slow.next
                curr = prev.next
            else:
                prev = prev.next
                curr = curr.next
            
            cnt += 1
        
        return head
