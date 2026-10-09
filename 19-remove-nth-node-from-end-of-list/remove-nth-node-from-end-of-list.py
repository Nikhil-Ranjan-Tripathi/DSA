# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        a = []
        while curr:
            a.append(curr.val)
            curr = curr.next
        
        n = -n
        a.pop(n)
        curr = head
        while curr.next:
            if a:
                curr = curr.next
                curr.val = a[0]
                a.pop(0)


        return head.next

