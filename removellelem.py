class Solution(object):
    def removeElements(self, head, val):
        dummy_head = ListNode(0)
        dummy_head.next = head
        current = dummy_head
       #create a dummy head, point it to head
       #iterate through LL and check vals
       #at the end return dummu_head.next because u need modified LL excluding dummy_head
        while current and current.next:
            if current.next.val == val:
                current.next=current.next.next
            else:
                current = current.next
        return dummy_head.next    
        
        
           
            
        #head->1->2->3->4->5->None