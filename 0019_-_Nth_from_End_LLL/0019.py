# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None and n == 1:
            return None

        count = self.removeHelper(head, n)

        if count == n:
            return head.next
        return head

    def removeHelper(self, node, n):
        if node is None:
            return 0

        count = self.removeHelper(node.next, n)

        if count == -1:
            return -1

        if count == n:
            node.next = node.next.next
            return -1

        return count + 1
