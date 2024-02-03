# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        
        #case when linkedlist is empty 
        if not head:
            return
        
        #case when Linked list has only one element
        if not head.next:
            return head
        
        #handle general case
        fpointer = head
        spointer = head

        while spointer is not None and spointer.next is not None:
            fpointer = fpointer.next
            spointer = spointer.next.next
        return fpointer
            