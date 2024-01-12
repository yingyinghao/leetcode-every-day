# 203. Remove Linked List Elements

# Given the head of a linlked list and an integer val, remove all
# the nodes of the listed list that has Node.val == val, and return the new head.

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 1. traverse the linked list
        # 2. remove the nodes of the linked list that has Node.val == val
        # 3. return the new head
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
