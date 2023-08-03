from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Two ptrs
        '''
        p, fast_p = head, head
        while fast_p and fast_p.next:
            p = p.next
            fast_p = fast_p.next.next
            if p == fast_p:
                return True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        '''
        Single ptr
        '''
        p = head
        while p:
            if p.val == None:
                return True
            p.val = None       # mark as visited
            p = p.next
        return False
