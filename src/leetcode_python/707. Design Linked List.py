# 707. Design Linked List
# https://leetcode.com/problems/design-linked-list/description/

class ListNode:
    def __init__(self,x):
        self.value=x
        self.next=None
        

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.dummy=ListNode(0)
        self.dummy.next=self.head
        
    def get(self, index: int) -> int:
        
        cur=self.dummy
        
        for i in range(index+1):
            cur=cur.next
            if not cur:
                return -1
            
        return cur.value
            
        
    def addAtHead(self, val: int) -> None:
        new=ListNode(val)
        new.next,self.dummy.next=self.dummy.next,new
    

       
    def addAtTail(self, val: int) -> None:
        
        new=ListNode(val)
        cur=self.dummy
        while cur.next:
            cur=cur.next
        cur.next=new
        
        
    def addAtIndex(self, index: int, val: int) -> None:
        new=ListNode(val)
        
        cur=self.dummy
        for i in range(index):
            cur=cur.next
            if not cur:
                return 
            
        new.next=cur.next
        cur.next=new

            
        

    def deleteAtIndex(self, index: int) -> None:

        cur=self.dummy
        
        for i in range(index):
            cur=cur.next
            if not cur:
                return 
            
        if not cur.next:
            return
        cur.next=cur.next.next
