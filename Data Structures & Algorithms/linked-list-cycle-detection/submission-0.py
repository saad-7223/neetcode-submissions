# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        seen = set()
        while pointer is not None:
            if pointer in seen:
                return True
            seen.add(pointer)
            pointer = pointer.next
        return False   