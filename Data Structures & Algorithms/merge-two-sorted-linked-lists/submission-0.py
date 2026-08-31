# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = list1
        
        head2 = list2
        head3 = ListNode()
        curr = head3
        
        
        while curr is not None:

            
            if head2 is None :
                curr.next = head1
                curr = head1
                break

            elif head1 is None :
                curr.next = head2
                curr = head2
                break

            
            elif head1.val <= head2.val:
                curr.next = head1
                curr = head1
                head1 = head1.next
                
            elif head2.val < head1.val:
                curr.next = head2
                curr = head2
                head2 = head2.next
        
        
        return head3.next
        