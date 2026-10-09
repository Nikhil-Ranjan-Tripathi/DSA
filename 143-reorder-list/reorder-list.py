# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next

        i, j = 0, len(a)-1
        c = []
        while i<=j:
            c.append(a[i])
            if i!=j:
                c.append(a[j])
            i+=1
            j-=1

        curr = head
        for val in c:
            curr.val = val
            curr = curr.next


        
        