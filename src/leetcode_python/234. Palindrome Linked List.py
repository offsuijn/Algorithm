# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        
        return True
