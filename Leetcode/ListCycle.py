# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False
            
        fast = slow = head

        # Slow moves one step at a time, fast - 2 steps at a time
        # If they will meet => we have a cycle. Otherwise, fast will reach the end
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow:
                return True
        
        return False
