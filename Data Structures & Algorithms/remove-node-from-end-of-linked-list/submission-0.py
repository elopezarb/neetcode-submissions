# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        if head is None:
            return None
        
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        new_head = ListNode()
        curr = new_head
        while curr is not None:
            curr.next = head
            if curr.next == slow:
                curr.next = slow.next
                break
            
            else:
                head = head.next
                curr = curr.next
        
        return new_head.next
        