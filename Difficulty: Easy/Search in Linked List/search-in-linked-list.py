'''Structure of Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        
        while head:
            if head.data==key:
                return True
            
            head = head.next
            
        return False