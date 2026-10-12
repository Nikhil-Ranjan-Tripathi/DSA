# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a1 = []
        a2 = []
        curr = head
        while curr:
            if curr in a1:
                return curr
            else:
                a1.append(curr)
                a2.append(curr.val)

            curr = curr.next

        return curr