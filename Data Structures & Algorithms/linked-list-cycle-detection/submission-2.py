# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        
        if head is None:
            return False
        if head.next is None:
            return False
        else:
            slow = head
            fast = head.next.next
            
        
        while slow is not None:
            
            
            if fast is None:
                break
            
            elif slow == fast:
                return True
            
            else:
                slow = slow.next
                
                if fast.next is None:
                    return False
                else:
                    fast = fast.next.next

        
        return False