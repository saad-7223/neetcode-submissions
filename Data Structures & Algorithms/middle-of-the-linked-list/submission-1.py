# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        count = 0
        while pointer is not None:
            count += 1
            pointer = pointer.next
        
        if count == 0 or count == 1:
            return head
            
        middle = count//2
        curr = head
        for i in range(middle-1):
            curr = curr.next

        head = curr.next
        return head