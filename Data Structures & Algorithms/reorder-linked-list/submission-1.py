# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head is None:
            return None
        head = head
        slow = head
        fast = head
        if slow.next is None:
            return None

        while fast is not None:
            if fast.next is None:
                break
            
            else:
                fast = fast.next.next
            slow = slow.next
        
        
        middle = slow
        middle_rev = self.reverseList(middle)
        
        new_head = ListNode()
        curr = new_head
        while middle_rev is not None:

            if head == middle:
                curr.next = middle_rev
                break
            curr.next = head
            head = head.next
            curr = curr.next
        
            curr.next = middle_rev
            middle_rev = middle_rev.next
            curr = curr.next
        
        return None
        