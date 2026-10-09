# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        while l1:
            a.append(l1.val)
            l1 = l1.next

        while l2:
            a.append(l2.val)
            l2 = l2.next

        a.sort()
        curr = ListNode(0)
        head = curr
        while a:
            head.next = ListNode(a[0])
            a.pop(0)
            head = head.next

        return curr.next











        # dummy = ListNode(0)
        # curr = dummy
        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         list2 = list2.next
        #     curr = curr.next

        # if list1:
        #     curr.next = list1
        # else:
        #     curr.next = list2

        # return dummy.next