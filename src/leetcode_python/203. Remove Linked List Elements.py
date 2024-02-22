# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        return dummy.next
