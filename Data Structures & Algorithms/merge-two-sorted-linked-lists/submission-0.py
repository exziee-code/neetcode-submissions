# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            c1 = list1
            c2 = list2
            if not c1:
                return c2
            elif not c2:
                return c1
            
            if c1.val <= c2.val:
                self.head = c1
                self.tail = c1
                c1 = c1.next
            else:
                self.head = c2
                self.tail = c2
                c2 = c2.next

            while c1 and c2:
                if c1.val <= c2.val:
                    self.tail.next = c1
                    self.tail = c1  
                    c1 = c1.next
                
                else:
                    self.tail.next = c2
                    self.tail = c2
                    c2 = c2.next
                
            if c1:
                self.tail.next = c1
            
            if c2:
                self.tail.next = c2
            
            return self.head